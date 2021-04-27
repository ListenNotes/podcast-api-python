from listennotes import podcast_api


class TestClient(object):
    def test_set_apikey(self):
        client = podcast_api.Client()
        assert client.request_headers.get("X-ListenAPI-Key") is None

        api_key = "abcd"
        client = podcast_api.Client(api_key=api_key)
        assert client.request_headers.get("X-ListenAPI-Key") == api_key

    def test_search(self):
        client = podcast_api.Client()
        response = client.search(q="dummy")
        assert len(response.json().get("results", [])) > 0
