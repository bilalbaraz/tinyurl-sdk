class TinyURLClientError(Exception):
    """Base error for TinyURL client operations."""


class TinyURLHTTPError(TinyURLClientError):
    """Raised when the HTTP layer fails or returns a non-200 response."""


class TinyURLResponseError(TinyURLClientError):
    """Raised when the API response is missing expected fields."""
