"""Opt-in HTTP tests against the stateless, public mock service."""

from urllib.parse import parse_qs, urlparse

import pytest
import requests

from listennotes import podcast_api
from listennotes.errors import NotFoundError

pytestmark = pytest.mark.integration

MOCK_BASE = "https://listen-api-test.listennotes.com/api/v2"
PLAYLIST_ID = "m1pe7z60bsw"
ITEM_ID = 23
EPISODE_ID = "e73b7e5695b44ab9b6c9ae6b7e0ac6e0"
PODCAST_ID = "4d3fe717742d4963a85562e9f84d8c79"


@pytest.fixture
def client(monkeypatch):
    client = podcast_api.Client(api_key=None, max_retries=0)
    assert client.api_base == MOCK_BASE
    session = client.http_client.session
    session.trust_env = False  # Ignore proxy settings and .netrc credentials.
    send = session.send

    def send_to_mock(request, **kwargs):
        # Validate the final prepared request before any network access.
        assert request.url.startswith(MOCK_BASE + "/")
        assert "X-ListenAPI-Key" not in request.headers
        assert "Authorization" not in request.headers
        kwargs["allow_redirects"] = False
        kwargs["timeout"] = (5, 15)
        return send(request, **kwargs)

    monkeypatch.setattr(session, "send", send_to_mock)
    yield client
    session.close()


def response_json(response, method, path, status=200):
    assert isinstance(response, requests.Response)
    assert response.status_code == status, response.text[:500]
    assert response.request.method == method
    assert urlparse(response.url).path == "/api/v2" + path
    assert response.headers["Content-Type"].startswith("application/json")
    assert int(response.headers["X-ListenAPI-Usage"]) >= 0
    assert int(response.headers["X-ListenAPI-FreeQuota"]) > 0
    assert float(response.headers["X-ListenAPI-Latency-Seconds"]) >= 0
    assert response.headers["X-ListenAPI-NextBillingDate"]
    payload = response.json()
    assert isinstance(payload, dict)
    return payload


def assert_playlist(payload):
    assert isinstance(payload["id"], str)
    assert payload["name"]
    assert payload["type"] in {"episode_list", "podcast_list"}
    assert payload["visibility"] in {"public", "unlisted", "private"}
    assert payload["listennotes_url"].startswith(
        "https://www.listennotes.com/"
    )


def assert_item(payload):
    assert isinstance(payload["id"], int)
    assert isinstance(payload["notes"], str)
    assert isinstance(payload["data"], dict)
    assert payload["type"] in {"episode", "podcast"}
    assert isinstance(payload["added_at_ms"], int)


def test_search(client):
    query = "science & café"
    response = client.search(q=query, sort_by_date=1)
    payload = response_json(response, "GET", "/search")
    assert payload["results"]
    assert parse_qs(urlparse(response.request.url).query) == {
        "q": [query],
        "sort_by_date": ["1"],
    }


def test_fetch_podcast(client):
    response = client.fetch_podcast_by_id(id=PODCAST_ID)
    payload = response_json(response, "GET", f"/podcasts/{PODCAST_ID}")
    assert payload["id"]
    assert isinstance(payload["episodes"], list)


def test_list_playlists(client):
    response = client.fetch_my_playlists()
    payload = response_json(response, "GET", "/playlists")
    assert payload["playlists"]
    assert_playlist(payload["playlists"][0])


def test_fetch_playlist(client):
    response = client.fetch_playlist_by_id(id=PLAYLIST_ID, type="episode_list")
    payload = response_json(response, "GET", f"/playlists/{PLAYLIST_ID}")
    assert_playlist(payload)
    assert isinstance(payload["items"], list)
    assert parse_qs(urlparse(response.request.url).query) == {
        "type": ["episode_list"]
    }


def test_create_playlist(client):
    response = client.create_playlist(
        name="Python SDK integration", description="", visibility="private"
    )
    payload = response_json(response, "POST", "/playlists", status=201)
    assert_playlist(payload)
    assert parse_qs(response.request.body, keep_blank_values=True) == {
        "name": ["Python SDK integration"],
        "description": [""],
        "visibility": ["private"],
    }


def test_update_playlist(client):
    response = client.update_playlist(
        id=PLAYLIST_ID, description="", type="podcast_list"
    )
    payload = response_json(response, "PUT", f"/playlists/{PLAYLIST_ID}")
    assert_playlist(payload)
    assert parse_qs(response.request.body, keep_blank_values=True) == {
        "description": [""],
        "type": ["podcast_list"],
    }


@pytest.mark.parametrize(
    "content", [{"episode_id": EPISODE_ID}, {"podcast_id": PODCAST_ID}]
)
def test_add_playlist_item(client, content):
    response = client.add_playlist_item(
        id=PLAYLIST_ID, notes="hello & café", **content
    )
    payload = response_json(
        response, "POST", f"/playlists/{PLAYLIST_ID}/items", status=201
    )
    assert_item(payload)
    assert parse_qs(response.request.body) == {
        **{key: [value] for key, value in content.items()},
        "notes": ["hello & café"],
    }


@pytest.mark.parametrize("notes", ["hello & café", ""])
def test_update_playlist_item_notes(client, notes):
    response = client.update_playlist_item_notes(
        id=PLAYLIST_ID, item_id=ITEM_ID, notes=notes
    )
    payload = response_json(
        response, "PUT", f"/playlists/{PLAYLIST_ID}/items/{ITEM_ID}"
    )
    assert_item(payload)
    assert parse_qs(response.request.body, keep_blank_values=True) == {
        "notes": [notes]
    }


def test_delete_playlist_item(client):
    response = client.delete_playlist_item(id=PLAYLIST_ID, item_id=ITEM_ID)
    payload = response_json(
        response, "DELETE", f"/playlists/{PLAYLIST_ID}/items/{ITEM_ID}"
    )
    assert payload["deleted"] is True
    assert isinstance(payload["id"], int)
    assert response.request.body is None


def test_missing_route(client):
    with pytest.raises(NotFoundError) as exc:
        client.http_client.get(MOCK_BASE + "/sdk-integration-missing-route")
    assert exc.value.response.status_code == 404
