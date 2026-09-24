"""HTTP transport and public API error translation."""

import requests
from requests import exceptions
from urllib3.util import Retry

from listennotes import errors


class Request:
    MAX_RETRIES = 3
    MAX_REDIRECTS = 15
    TIMEOUT = 30
    READ_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})

    def __init__(
        self,
        max_redirects=MAX_REDIRECTS,
        max_retries=MAX_RETRIES,
        adapter=None,
        raise_exception=True,
        **kwargs,
    ):
        self.session = requests.Session()
        self.raise_exception = raise_exception
        # Connection-establishment retries are safe before a request is sent.
        # Only reads may retry ambiguous response failures or Retry-After statuses.
        if adapter is None:
            adapter = requests.adapters.HTTPAdapter(
                max_retries=Retry(
                    total=max_retries,
                    allowed_methods=self.READ_METHODS,
                    other=0,
                )
            )
        for key, value in kwargs.items():
            if hasattr(self.session, key):
                setattr(self.session, key, value)
        self.session.max_redirects = max_redirects
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def request(self, method, url, timeout=TIMEOUT, **kwargs):
        if method.upper() not in self.READ_METHODS:
            kwargs.setdefault("allow_redirects", False)
        try:
            response = self.session.request(
                method, url, timeout=timeout, **kwargs
            )
        except (exceptions.ConnectionError, exceptions.Timeout) as exc:
            if not self.raise_exception:
                raise
            raise errors.APIConnectionError(
                "Failed to connect to Listen API.", response=exc.response
            ) from exc

        if self.raise_exception:
            try:
                response.raise_for_status()
            except exceptions.HTTPError:
                error_type, message = {
                    400: (
                        errors.InvalidRequestError,
                        "Invalid request parameters.",
                    ),
                    401: (
                        errors.AuthenticationError,
                        "Wrong API key or suspended account.",
                    ),
                    403: (
                        errors.PermissionDeniedError,
                        "Permission denied for this resource.",
                    ),
                    404: (
                        errors.NotFoundError,
                        "Endpoint or requested resource not found.",
                    ),
                    429: (
                        errors.RateLimitError,
                        "API quota or rate limit exceeded.",
                    ),
                }.get(response.status_code, (None, None))
                if response.status_code >= 500:
                    error_type = errors.ListenApiError
                    message = "Unexpected Listen API server error."
                if error_type is None:
                    raise
                try:
                    payload = response.json()
                except ValueError:
                    payload = None
                if isinstance(payload, dict) and isinstance(
                    payload.get("error"), str
                ):
                    message = payload["error"] or message
                raise error_type(message, response=response) from None
        return response

    def delete(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("DELETE", url, timeout, **kwargs)

    def get(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("GET", url, timeout, **kwargs)

    def head(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("HEAD", url, timeout, **kwargs)

    def options(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("OPTIONS", url, timeout, **kwargs)

    def patch(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("PATCH", url, timeout, **kwargs)

    def post(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("POST", url, timeout, **kwargs)

    def put(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("PUT", url, timeout, **kwargs)

    def trace(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("TRACE", url, timeout, **kwargs)

    def purge(self, url, timeout=TIMEOUT, **kwargs):
        return self.request("PURGE", url, timeout, **kwargs)
