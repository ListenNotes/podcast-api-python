import requests
from requests import exceptions

from listennotes import errors


class Request:
    """Making HTTP requests.

    Apply the best practices of making http requests:
    1. timeout
    2. retry
    3. max redirects
    4. exposes python-request exceptions, callers are responsible
    to handle them.
    """

    MAX_RETRIES = 3
    MAX_REDIRECTS = 15
    TIMEOUT = 30  # seconds

    def __init__(
        self,
        max_redirects=MAX_REDIRECTS,
        max_retries=MAX_RETRIES,
        adapter=None,
        raise_exception=True,
        **kwargs
    ):
        """Set up a requests.Session object.

        Args:
            max_redirects: max redirects.
            max_retries: max retries.
            adapter: a custom requests.adapters.HTTPAdapter object.
                If this argument is specified, max_retries argument is ignored.
            kwargs: keyword args to set session attribute, e.g., auth.
        """
        self.session = requests.Session()
        self.raise_exception = raise_exception
        if not adapter:
            the_adapter = requests.adapters.HTTPAdapter(
                max_retries=max_retries
            )
        else:
            the_adapter = adapter

        for key, value in kwargs.items():
            if hasattr(self.session, key):
                setattr(self.session, key, value)

        self.session.max_redirects = max_redirects
        self.session.mount("http://", the_adapter)
        self.session.mount("https://", the_adapter)

    def request(self, method, url, timeout=TIMEOUT, **kwargs):
        """Make a http(s) request.

        Args:
            method: http method name, should be one of DELETE', 'GET', 'HEAD',
                'OPTIONS', 'PATCH', 'POST', 'PUT', and 'TRACE'.
            url: the url to request.
            timeout: request timeout.
            kwargs: keyword arguments.

        Returns:
            a response object.

        Raises:
            requests.exceptions.RequestException if there was an ambiguous
                exception that occurred while handling your request. This is
                the base class for all the following exceptions.

            requests.exceptions.ConnectionError if a Connection error occurred,
                e.g., DNS failure, refused connection, etc.

            requests.exceptions.HTTPError if an HTTP error occurred, i.e.,
                status code is 4xx or 5xx.

            requests.exceptions.URLRequired if a valid URL is required to make,
                a request.

            requests.exceptions.TooManyRedirects if too many redirects.
        """
        the_headers = {}
        if "headers" in kwargs:
            the_headers.update(kwargs["headers"])
            del kwargs["headers"]

        response = self.session.request(
            method, url, timeout=timeout, headers=the_headers, **kwargs
        )
        # If response.status_code is 4xx or 5xx, raise
        # requests.exceptions.HTTPError
        if self.raise_exception:
            try:
                response.raise_for_status()
            except exceptions.ConnectionError:
                raise errors.APIConnectionError(
                    "Failed to connect to Listen API", response=response
                ) from None
            except exceptions.HTTPError as e:
                status_code = e.response.status_code
                if status_code == 404:
                    # from None => suppress previous exception
                    raise errors.NotFoundError(
                        "Endpoint not exist, or podcast / episode not exist",
                        response=response,
                    ) from None
                elif status_code == 401:
                    raise errors.AuthenticationError(
                        "Wrong api key or your account is suspended",
                        response=response,
                    ) from None
                elif status_code == 429:
                    raise errors.RateLimitError(
                        "You use FREE plan and you exceed the quota limit",
                        response=response,
                    ) from None
                elif status_code == 400:
                    raise errors.InvalidRequestError(
                        "Something wrong on your end (client side errors),"
                        " e.g., missing required parameters",
                        response=response,
                    ) from None
                elif status_code >= 500:
                    raise errors.ListenApiError(
                        "Error on our end (unexpected server errors)",
                        response=response,
                    ) from None
                else:
                    raise
            except Exception:
                raise errors.ListenApiError(
                    "Unknown error. Please report to hello@listennotes.com",
                    response=response,
                ) from None

        return response

    def delete(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for DELETE request."""
        return self.request("DELETE", url, timeout, **kwargs)

    def get(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for GET request."""
        return self.request("GET", url, timeout, **kwargs)

    def head(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for HEAD request."""
        return self.request("HEAD", url, timeout, **kwargs)

    def options(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for OPTIONS request."""
        return self.request("OPTIONS", url, timeout, **kwargs)

    def patch(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for PATCH request."""
        return self.request("PATCH", url, timeout, **kwargs)

    def post(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for POST request."""
        return self.request("POST", url, timeout, **kwargs)

    def put(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for PUT request."""
        return self.request("PUT", url, timeout, **kwargs)

    def trace(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for TRACE request."""
        return self.request("TRACE", url, timeout, **kwargs)

    def purge(self, url, timeout=TIMEOUT, **kwargs):
        """Shortcut for TRACE request."""
        return self.request("PURGE", url, timeout, **kwargs)
