class ListenApiError(Exception):
    """
    Display a very generic error to the user
    """

    def __init__(self, message=None, response=None):
        super(ListenApiError, self).__init__(message)
        self._message = message
        self.response = response

    def __str__(self):
        return self._message


class NotFoundError(ListenApiError):
    """
    Endpoint not exist or the podcast / episode not exist
    """

    pass


class InvalidRequestError(ListenApiError):
    """
    Invalid parameters were supplied to Listen API
    """

    pass


class AuthenticationError(ListenApiError):
    """
    Authentication with Listen API failed
    """

    pass


class RateLimitError(ListenApiError):
    """
    For FREE plan, exceeding the quota limit; or for all plans,
    sending too many requests too fast and exceeding the rate limit
    - https://www.listennotes.com/api/faq/#faq17
    """

    pass


class APIConnectionError(ListenApiError):
    """
    Network communication with Listen API failed
    """

    pass
