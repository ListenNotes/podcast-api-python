import copy
from importlib.resources import files
import json
from urllib.parse import parse_qs, quote, urlparse

import pytest
import requests

from listennotes import podcast_api

CONTRACT = json.loads(
    files("listennotes").joinpath("api-contract.json").read_text()
)
OPERATIONS = CONTRACT["operations"]


def normalized(values):
    result = {}
    for key, value in values.items():
        if value is None:
            continue
        if isinstance(value, (list, tuple)):
            result[key] = [str(item) for item in value]
        else:
            result[key] = [str(value)]
    return result


@pytest.mark.parametrize("operation", OPERATIONS, ids=lambda op: op["func"])
def test_every_generated_method_against_contract(operation, transport):
    client = podcast_api.Client(api_key="test-key")
    params = copy.deepcopy(operation["example_params"])
    before = copy.deepcopy(params)
    response = getattr(client, operation["func"])(**params)
    request, options = transport.calls[0]
    assert len(transport.calls) == 1
    assert request.method == operation["method"]
    path = operation["path"]
    for param in operation["parameters"]:
        if param["in"] == "path":
            path = path.replace(
                "{" + param["name"] + "}",
                quote(str(params[param["name"]]), safe=""),
            )
    assert urlparse(request.url).path == "/api/v2" + path
    for location, encoded in (
        ("query", urlparse(request.url).query),
        ("body", request.body or ""),
    ):
        expected = {
            param["name"]: params[param["name"]]
            for param in operation["parameters"]
            if param["in"] == location and param["name"] in params
        }
        assert parse_qs(encoded, keep_blank_values=True) == normalized(
            expected
        )
    assert request.headers["X-ListenAPI-Key"] == "test-key"
    assert options["timeout"] == 30
    assert isinstance(response, requests.Response)
    assert response.json() == {"ok": True}
    assert response.headers["X-ListenAPI-Usage"] == "42"
    assert params == before


def test_nested_path_ids_and_empty_notes(transport):
    client = podcast_api.Client(api_key="test-key")
    client.update_playlist_item_notes(id="a/b ?#%", item_id="23/4", notes="")
    request = transport.calls[0][0]
    assert request.url.endswith("/playlists/a%2Fb%20%3F%23%25/items/23%2F4")
    assert request.body == "notes="
    assert (
        request.headers["Content-Type"] == "application/x-www-form-urlencoded"
    )


def test_query_encoding_and_forward_compatible_fields(transport):
    client = podcast_api.Client()
    client.search(
        q="a+b & café", offset=0, safe_mode=False, future="", ignored=None
    )
    request = transport.calls[0][0]
    assert parse_qs(urlparse(request.url).query, keep_blank_values=True) == {
        "q": ["a+b & café"],
        "offset": ["0"],
        "safe_mode": ["False"],
        "future": [""],
    }
    assert "X-ListenAPI-Key" not in request.headers
    assert request.url.startswith(podcast_api.api_base_test)


def test_delete_podcast_reason_is_query_not_body(transport):
    podcast_api.Client().delete_podcast(id="abc", reason="a & b")
    request = transport.calls[0][0]
    assert request.method == "DELETE"
    assert request.url.endswith("/podcasts/abc?reason=a+%26+b")
    assert request.body is None


def test_query_and_body_are_routed_independently(transport):
    client = podcast_api.Client()
    client._request_api(
        "PUT",
        "/example/{id}",
        ("locale",),
        {
            "id": "a/b",
            "locale": "en",
            "description": "",
            "extra": 0,
            "skip": None,
        },
    )
    request = transport.calls[0][0]
    assert request.url.endswith("/example/a%2Fb?locale=en")
    assert parse_qs(request.body, keep_blank_values=True) == {
        "description": [""],
        "extra": ["0"],
    }


@pytest.mark.parametrize("status", [200, 201])
def test_add_item_duplicate_or_created_response(status, transport):
    transport.status = status
    transport.payload = {"id": 23, "notes": ""}
    result = podcast_api.Client().add_playlist_item(
        id="playlist", episode_id="episode"
    )
    assert result.status_code == status
    assert result.json() == {"id": 23, "notes": ""}
    assert transport.calls[0][0].body == "episode_id=episode"


@pytest.mark.parametrize("notes", [None, "", "hello & goodbye"])
def test_optional_notes_preserve_omission_and_empty_string(notes, transport):
    podcast_api.Client().add_playlist_item(
        id="playlist", podcast_id="podcast", notes=notes
    )
    fields = parse_qs(transport.calls[0][0].body, keep_blank_values=True)
    assert fields["podcast_id"] == ["podcast"]
    assert "episode_id" not in fields
    if notes is None:
        assert "notes" not in fields
    else:
        assert fields["notes"] == [notes]


def test_metadata_clearing_and_type(transport):
    podcast_api.Client().update_playlist(
        id="playlist", description="", type="podcast_list"
    )
    request = transport.calls[0][0]
    assert parse_qs(request.body, keep_blank_values=True) == {
        "description": [""],
        "type": ["podcast_list"],
    }


@pytest.mark.parametrize("field", ["id", "item_id"])
@pytest.mark.parametrize("value", [None, ""])
def test_missing_path_parameter_fails_before_http(field, value, transport):
    params = {"id": "playlist", "item_id": 23}
    params[field] = value
    with pytest.raises(ValueError, match=f"Missing path parameter: {field}"):
        podcast_api.Client().delete_playlist_item(**params)
    assert not transport.calls


def test_clients_keep_independent_keys_sessions_and_configuration(transport):
    first = podcast_api.Client(
        api_key="first", user_agent="first-agent", max_retries=0
    )
    second = podcast_api.Client(api_key="second", max_retries=2)
    mock = podcast_api.Client()
    first.fetch_my_playlists()
    second.fetch_my_playlists()
    mock.fetch_my_playlists()
    assert [
        call[0].headers.get("X-ListenAPI-Key") for call in transport.calls
    ] == ["first", "second", None]
    assert transport.calls[0][0].headers["User-Agent"] == "first-agent"
    assert (
        transport.calls[1][0].headers["User-Agent"]
        == "podcast-api-python 3.0.0"
    )
    assert first.http_client.session is not second.http_client.session
    assert (
        first.http_client.session.get_adapter("https://").max_retries.total
        == 0
    )
    assert (
        second.http_client.session.get_adapter("https://").max_retries.total
        == 2
    )
    assert first.api_base == second.api_base == podcast_api.api_base_prod
    assert mock.api_base == podcast_api.api_base_test
