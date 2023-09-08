from urllib.parse import parse_qs, urlparse

from listennotes import podcast_api
from listennotes.errors import AuthenticationError


class TestClient(object):
    def test_set_apikey(self):
        client = podcast_api.Client()
        assert client.request_headers.get("X-ListenAPI-Key") is None

        api_key = "abcd"
        client = podcast_api.Client(api_key=api_key)
        assert client.request_headers.get("X-ListenAPI-Key") == api_key

    def test_search_with_mock(self):
        client = podcast_api.Client()
        term = "dummy"
        sort_by_date = 1
        response = client.search(q=term, sort_by_date=sort_by_date)
        assert len(response.json().get("results", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/search"
        params = parse_qs(url.query)
        assert params["q"][0] == term
        assert params["sort_by_date"][0] == "1"

    def test_search_with_authentication_error(self):
        api_key = "wrong key"
        client = podcast_api.Client(api_key=api_key)
        term = "dummy"
        sort_by_date = 1
        try:
            client.search(q=term, sort_by_date=sort_by_date)
        except AuthenticationError:
            pass
        except Exception:
            assert False
        else:
            assert False

    def test_search_episode_titles_with_mock(self):
        client = podcast_api.Client()
        term = "dummy2"
        response = client.search_episode_titles(
            q=term, podcast_id='0cdaa63b905b4de3861554669a6a3dd1')
        assert len(response.json().get("results", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/search_episode_titles"
        params = parse_qs(url.query)
        assert params["q"][0] == term
        assert params["podcast_id"][0] == "0cdaa63b905b4de3861554669a6a3dd1"

    def test_typeahead_with_mock(self):
        client = podcast_api.Client()
        term = "dummy"
        show_podcasts = 1
        response = client.typeahead(q=term, show_podcasts=show_podcasts)
        assert len(response.json().get("terms", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/typeahead"
        params = parse_qs(url.query)
        assert params["q"][0] == term
        assert params["show_podcasts"][0] == "1"

    def test_spellcheck_with_mock(self):
        client = podcast_api.Client()
        term = "dummy"
        response = client.spellcheck(q=term)
        assert len(response.json().get("tokens", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/spellcheck"
        params = parse_qs(url.query)
        assert params["q"][0] == term

    def test_related_searches_with_mock(self):
        client = podcast_api.Client()
        term = "dummy"
        response = client.fetch_related_searches(q=term)
        assert len(response.json().get("terms", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/related_searches"
        params = parse_qs(url.query)
        assert params["q"][0] == term

    def test_trending_searches_with_mock(self):
        client = podcast_api.Client()
        response = client.fetch_trending_searches()
        assert len(response.json().get("terms", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/trending_searches"

    def test_fetch_best_podcasts_with_mock(self):
        client = podcast_api.Client()
        genre_id = 23
        response = client.fetch_best_podcasts(genre_id=genre_id)
        assert response.json().get("total", 0) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/best_podcasts"
        params = parse_qs(url.query)
        assert params["genre_id"][0] == str(genre_id)

    def test_fetch_podcast_by_id_with_mock(self):
        client = podcast_api.Client()
        podcast_id = "asdfsdaf"
        response = client.fetch_podcast_by_id(id=podcast_id)
        assert len(response.json().get("episodes", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/podcasts/%s" % podcast_id

    def test_fetch_episode_by_id_with_mock(self):
        client = podcast_api.Client()
        episode_id = "asdfsdaf"
        response = client.fetch_episode_by_id(id=episode_id)
        assert len(response.json().get("podcast", {}).get("rss")) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/episodes/%s" % episode_id

    def test_batch_fetch_podcasts_with_mock(self):
        client = podcast_api.Client()
        ids = "996,777,888,1000"
        response = client.batch_fetch_podcasts(ids=ids)
        assert parse_qs(response.request.body)["ids"][0] == ids
        assert len(response.json().get("podcasts", [])) > 0
        assert response.request.method == "POST"
        url = urlparse(response.url)
        assert url.path == "/api/v2/podcasts"

    def test_batch_fetch_episodes_with_mock(self):
        client = podcast_api.Client()
        ids = "996,777,888,100220"
        response = client.batch_fetch_episodes(ids=ids)
        assert parse_qs(response.request.body)["ids"][0] == ids
        assert len(response.json().get("episodes", [])) > 0
        assert response.request.method == "POST"
        url = urlparse(response.url)
        assert url.path == "/api/v2/episodes"

    def test_fetch_curated_podcasts_list_by_id_with_mock(self):
        client = podcast_api.Client()
        curated_list_id = "asdfsdaf"
        response = client.fetch_curated_podcasts_list_by_id(id=curated_list_id)
        assert len(response.json().get("podcasts", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/curated_podcasts/%s" % curated_list_id

    def test_fetch_curated_podcasts_lists_with_mock(self):
        client = podcast_api.Client()
        page = 2
        response = client.fetch_curated_podcasts_lists(page=page)
        assert response.json().get("total") > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        params = parse_qs(url.query)
        assert params["page"][0] == str(page)
        assert url.path == "/api/v2/curated_podcasts"

    def test_fetch_podcast_genres_with_mock(self):
        client = podcast_api.Client()
        top_level_only = 1
        response = client.fetch_podcast_genres(top_level_only=top_level_only)
        assert len(response.json().get("genres", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        params = parse_qs(url.query)
        assert params["top_level_only"][0] == str(top_level_only)
        assert url.path == "/api/v2/genres"

    def test_fetch_podcast_regions_with_mock(self):
        client = podcast_api.Client()
        response = client.fetch_podcast_regions()
        assert len(response.json().get("regions", {}).keys()) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/regions"

    def test_fetch_podcast_languages_with_mock(self):
        client = podcast_api.Client()
        response = client.fetch_podcast_languages()
        assert len(response.json().get("languages", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/languages"

    def test_just_listen_with_mock(self):
        client = podcast_api.Client()
        response = client.just_listen()
        assert response.json().get("audio_length_sec", 0) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/just_listen"

    def test_fetch_recommendations_for_podcast_with_mock(self):
        client = podcast_api.Client()
        podcast_id = "adfsddf"
        response = client.fetch_recommendations_for_podcast(id=podcast_id)
        assert len(response.json().get("recommendations", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/podcasts/%s/recommendations" % podcast_id

    def test_fetch_recommendations_for_episode_with_mock(self):
        client = podcast_api.Client()
        episode_id = "adfsddf"
        response = client.fetch_recommendations_for_episode(id=episode_id)
        assert len(response.json().get("recommendations", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/episodes/%s/recommendations" % episode_id

    def test_fetch_playlist_by_id_with_mock(self):
        client = podcast_api.Client()
        playlist_id = "adfsddf"
        response = client.fetch_playlist_by_id(id=playlist_id)
        assert len(response.json().get("items", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/playlists/%s" % playlist_id

    def test_fetch_my_playlists_with_mock(self):
        client = podcast_api.Client()
        page = 2
        response = client.fetch_my_playlists(page=page)
        assert len(response.json().get("playlists", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/playlists"

    def test_submit_podcast_with_mock(self):
        client = podcast_api.Client()
        rss = "http://myrss.com/rss"
        response = client.submit_podcast(rss=rss)
        assert parse_qs(response.request.body)["rss"][0] == rss
        assert len(response.json().get("status", "")) > 0
        assert response.request.method == "POST"
        url = urlparse(response.url)
        assert url.path == "/api/v2/podcasts/submit"

    def test_delete_podcast_with_mock(self):
        client = podcast_api.Client()
        podcast_id = "asdfasdfdf"
        response = client.delete_podcast(id=podcast_id)
        assert len(response.json().get("status", "")) > 0
        assert response.request.method == "DELETE"
        url = urlparse(response.url)
        assert url.path == "/api/v2/podcasts/%s" % podcast_id

    def test_fetch_audience_for_podcast_with_mock(self):
        client = podcast_api.Client()
        podcast_id = "adfsddf"
        response = client.fetch_audience_for_podcast(id=podcast_id)
        assert len(response.json().get("by_regions", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        assert url.path == "/api/v2/podcasts/%s/audience" % podcast_id

    def test_fetch_podcasts_by_domain_with_mock(self):
        client = podcast_api.Client()
        domain_name = "nytimes.com"
        response = client.fetch_podcasts_by_domain(domain_name=domain_name, page=3)
        assert len(response.json().get("podcasts", [])) > 0
        assert response.request.method == "GET"
        url = urlparse(response.url)
        params = parse_qs(url.query)
        assert params["page"][0] == '3'
        assert url.path == "/api/v2/podcasts/domains/%s" % domain_name
