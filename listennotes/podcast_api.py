from listennotes import version, http_utils


api_key = None
api_base_prod = "https://listen-api.listennotes.com/api/v2"
api_base_test = "https://listen-api-test.listennotes.com/api/v2"
default_user_agent = "podcasts-api-python %s" % version.VERSION


class Client(object):
    def __init__(self, api_key=None, user_agent=None, max_retries=None):
        self.api_base = api_base_prod if api_key else api_base_test

        self.request_headers = {
            "X-ListenAPI-Key": api_key,
            "User-Agent": user_agent if user_agent else default_user_agent,
        }

        request_kwargs = {}
        if max_retries:
            request_kwargs["max_retries"] = max_retries

        self.http_client = http_utils.Request(**request_kwargs)

    #
    # All endpoints
    #
    def search(self, **kwargs):
        return self.http_client.get(
            "%s/search" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def typeahead(self, **kwargs):
        return self.http_client.get(
            "%s/typeahead" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def spellcheck(self, **kwargs):
        return self.http_client.get(
            "%s/spellcheck" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_related_searches(self, **kwargs):
        return self.http_client.get(
            "%s/related_searches" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_trending_searches(self, **kwargs):
        return self.http_client.get(
            "%s/trending_searches" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_best_podcasts(self, **kwargs):
        return self.http_client.get(
            "%s/best_podcasts" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_podcast_by_id(self, **kwargs):
        podcast_id = kwargs.pop("id", None)
        return self.http_client.get(
            "%s/podcasts/%s" % (self.api_base, podcast_id),
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_episode_by_id(self, **kwargs):
        episode_id = kwargs.pop("id", None)
        return self.http_client.get(
            "%s/episodes/%s" % (self.api_base, episode_id),
            params=kwargs,
            headers=self.request_headers,
        )

    def batch_fetch_podcasts(self, **kwargs):
        return self.http_client.post(
            "%s/podcasts" % self.api_base,
            data=kwargs,
            headers=self.request_headers,
        )

    def batch_fetch_episodes(self, **kwargs):
        return self.http_client.post(
            "%s/episodes" % self.api_base,
            data=kwargs,
            headers=self.request_headers,
        )

    def fetch_curated_podcasts_list_by_id(self, **kwargs):
        curated_list_id = kwargs.pop("id", None)
        return self.http_client.get(
            "%s/curated_podcasts/%s" % (self.api_base, curated_list_id),
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_curated_podcasts_lists(self, **kwargs):
        return self.http_client.get(
            "%s/curated_podcasts" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_podcast_genres(self, **kwargs):
        return self.http_client.get(
            "%s/genres" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_podcast_regions(self, **kwargs):
        return self.http_client.get(
            "%s/regions" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_podcast_languages(self, **kwargs):
        return self.http_client.get(
            "%s/languages" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def just_listen(self, **kwargs):
        return self.http_client.get(
            "%s/just_listen" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_recommendations_for_podcast(self, **kwargs):
        podcast_id = kwargs.pop("id", None)
        return self.http_client.get(
            "%s/podcasts/%s/recommendations" % (self.api_base, podcast_id),
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_recommendations_for_episode(self, **kwargs):
        episode_id = kwargs.pop("id", None)
        return self.http_client.get(
            "%s/episodes/%s/recommendations" % (self.api_base, episode_id),
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_playlist_by_id(self, **kwargs):
        playlist_id = kwargs.pop("id", None)
        return self.http_client.get(
            "%s/playlists/%s" % (self.api_base, playlist_id),
            params=kwargs,
            headers=self.request_headers,
        )

    def fetch_my_playlists(self, **kwargs):
        return self.http_client.get(
            "%s/playlists" % self.api_base,
            params=kwargs,
            headers=self.request_headers,
        )

    def submit_podcast(self, **kwargs):
        return self.http_client.post(
            "%s/podcasts/submit" % self.api_base,
            data=kwargs,
            headers=self.request_headers,
        )

    def delete_podcast(self, **kwargs):
        podcast_id = kwargs.pop("id", None)
        return self.http_client.delete(
            "%s/podcasts/%s" % (self.api_base, podcast_id),
            params=kwargs,
            headers=self.request_headers,
        )
