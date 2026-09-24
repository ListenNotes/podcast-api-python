"""Listen Notes API client. Endpoint methods are generated from OpenAPI."""

import re
from urllib.parse import quote

from listennotes import version, http_utils
from listennotes._api_methods import ApiMethods

api_key = None
api_base_prod = "https://listen-api.listennotes.com/api/v2"
api_base_test = "https://listen-api-test.listennotes.com/api/v2"
default_user_agent = "podcasts-api-python %s" % version.VERSION


class Client(ApiMethods):
    def __init__(self, api_key=None, user_agent=None, max_retries=None):
        self.api_base = api_base_prod if api_key else api_base_test
        self.request_headers = {
            "X-ListenAPI-Key": api_key,
            "User-Agent": user_agent if user_agent else default_user_agent,
        }
        request_kwargs = {}
        if max_retries is not None:
            request_kwargs["max_retries"] = max_retries
        self.http_client = http_utils.Request(**request_kwargs)

    def _request_api(self, method, template, query_names, values):
        params = dict(values)

        def path_value(match):
            name = match.group(1)
            value = params.pop(name, None)
            if value is None or value == "":
                raise ValueError(f"Missing path parameter: {name}")
            return quote(str(value), safe="")

        path = re.sub(r"\{([^}]+)\}", path_value, template)
        query, body = {}, {}
        for name, value in params.items():
            if value is None:
                continue
            # Unknown fields retain historical routing for forward compatibility.
            target = (
                query
                if name in query_names or method in {"GET", "DELETE"}
                else body
            )
            target[name] = value
        options = {"params": query, "headers": self.request_headers}
        if method in {"POST", "PUT"}:
            options["data"] = body
        return self.http_client.request(
            method, self.api_base + path, **options
        )
