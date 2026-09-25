import pytest
import requests
from urllib3.exceptions import ReadTimeoutError

from listennotes import errors, http_utils, podcast_api


@pytest.mark.parametrize(
    "status,error_class",
    [
        (400, errors.InvalidRequestError),
        (401, errors.AuthenticationError),
        (403, errors.PermissionDeniedError),
        (404, errors.NotFoundError),
        (429, errors.RateLimitError),
        (500, errors.ListenApiError),
        (503, errors.ListenApiError),
    ],
)
def test_http_errors_preserve_server_message_and_response(
    status, error_class, transport
):
    transport.status = status
    transport.payload = {"error": "Episode not found: missing-id."}
    with pytest.raises(
        error_class, match="Episode not found: missing-id"
    ) as captured:
        podcast_api.Client().add_playlist_item(
            id="playlist", episode_id="missing-id"
        )
    assert captured.value.response.status_code == status
    assert captured.value.response.json() == transport.payload


@pytest.mark.parametrize(
    "payload", [{}, {"error": None}, {"error": {"message": "nested"}}, []]
)
def test_unexpected_error_json_has_safe_fallback(payload, transport):
    transport.status = 404
    transport.payload = payload
    with pytest.raises(
        errors.NotFoundError, match="requested resource not found"
    ):
        podcast_api.Client().fetch_my_playlists()


def test_non_json_error_and_unmapped_http_status(transport):
    transport.status = 500
    transport.raw = b"<html>gateway error</html>"
    with pytest.raises(errors.ListenApiError, match="server error"):
        podcast_api.Client().fetch_my_playlists()
    transport.status = 418
    with pytest.raises(requests.exceptions.HTTPError):
        podcast_api.Client().fetch_my_playlists()


@pytest.mark.parametrize(
    "error", [requests.exceptions.ConnectionError, requests.exceptions.Timeout]
)
def test_transport_errors_are_translated(error, transport):
    transport.error = error("test network failure")
    with pytest.raises(errors.APIConnectionError) as captured:
        podcast_api.Client().fetch_my_playlists()
    assert captured.value.__cause__ is transport.error
    assert captured.value.response is None


def test_raise_exception_false_keeps_raw_response_and_transport_error(
    transport,
):
    client = http_utils.Request(raise_exception=False)
    transport.status = 403
    assert client.get("https://example.test").status_code == 403
    transport.error = requests.exceptions.ConnectionError("offline")
    with pytest.raises(requests.exceptions.ConnectionError):
        client.get("https://example.test")


@pytest.mark.parametrize("method", ["POST", "PUT", "DELETE"])
def test_writes_do_not_follow_redirects_or_retry_response_failures(
    method, transport
):
    client = http_utils.Request(max_retries=3)
    transport.status = 307
    # A redirect target must not receive the API key or replay the write.
    original_send = transport.send

    def redirect(*args, **kwargs):
        response = original_send(*args, **kwargs)
        response.headers["Location"] = "https://other.test/replayed"
        return response

    transport.send = redirect
    response = client.request(
        method,
        "https://example.test/resource",
        headers={"X-ListenAPI-Key": "key"},
    )
    assert response.status_code == 307
    assert len(transport.calls) == 1
    retry = client.session.get_adapter("https://").max_retries
    assert not retry.is_retry(method, 503, has_retry_after=True)
    with pytest.raises(ReadTimeoutError):
        retry.increment(
            method,
            "/resource",
            error=ReadTimeoutError(None, "/resource", "timeout"),
        )


def test_read_response_retries_remain_enabled_and_zero_disables_them():
    retry = (
        http_utils.Request(max_retries=2)
        .session.get_adapter("https://")
        .max_retries
    )
    assert retry.is_retry("GET", 503, has_retry_after=True)
    assert (
        retry.increment(
            "GET", "/", error=ReadTimeoutError(None, "/", "timeout")
        ).total
        == 1
    )
    disabled = (
        podcast_api.Client(max_retries=0)
        .http_client.session.get_adapter("https://")
        .max_retries
    )
    assert disabled.total == 0


@pytest.mark.parametrize(
    "method",
    [
        "delete",
        "get",
        "head",
        "options",
        "patch",
        "post",
        "put",
        "trace",
        "purge",
    ],
)
def test_http_shortcuts_pass_method_timeout_and_options(method, transport):
    getattr(http_utils.Request(), method)(
        "https://example.test", timeout=7, params={"q": "a b"}
    )
    request, options = transport.calls[0]
    assert request.method == method.upper()
    assert request.url == "https://example.test/?q=a+b"
    assert options["timeout"] == 7


def test_custom_adapter_and_session_settings():
    adapter = requests.adapters.HTTPAdapter(max_retries=0)
    request = http_utils.Request(
        adapter=adapter, max_redirects=2, trust_env=False
    )
    assert request.session.get_adapter("https://") is adapter
    assert request.session.max_redirects == 2
    assert not request.session.trust_env


def test_exception_without_message_is_printable():
    assert str(errors.ListenApiError()) == ""


@pytest.mark.parametrize(
    "method,params,attempts",
    [
        ("fetch_my_playlists", {}, 4),
        ("create_playlist", {"name": "test"}, 1),
        ("update_playlist", {"id": "playlist", "description": ""}, 1),
        ("delete_playlist", {"id": "playlist"}, 1),
        ("delete_playlist_item", {"id": "playlist", "item_id": 23}, 1),
    ],
)
def test_real_retry_pipeline_returns_final_error_without_replaying_writes(
    method, params, attempts, monkeypatch
):
    import io
    from urllib3.response import HTTPResponse

    client = podcast_api.Client(api_key="test-key")
    client.http_client.session.trust_env = False
    adapter = client.http_client.session.get_adapter("https://")
    pool = adapter.poolmanager.connection_from_url(client.api_base)
    calls = []

    def unavailable(*args, **kwargs):
        calls.append(1)
        return HTTPResponse(
            status=503,
            headers={"Retry-After": "0", "Content-Type": "application/json"},
            body=io.BytesIO(b'{"error": "Temporarily unavailable."}'),
            preload_content=False,
        )

    monkeypatch.setattr(pool, "_make_request", unavailable)
    monkeypatch.setattr(
        adapter,
        "get_connection_with_tls_context",
        lambda *args, **kwargs: pool,
    )
    with pytest.raises(
        errors.ListenApiError, match="Temporarily unavailable"
    ) as captured:
        getattr(client, method)(**params)
    assert captured.value.response.status_code == 503
    assert len(calls) == attempts
