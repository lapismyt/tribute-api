from tribute_api.base.exceptions import TributeApiBaseError
from tribute_api.v1.models.enums import TributeErrorCode


class TributeApiV1Exception(TributeApiBaseError):
    """Base exception for all v1 API exceptions."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return (
            f"{self.error_code}: {self.message}"
            if self.message
            else str(self.error_code)
        )


class TributeApiV1BadRequest(TributeApiV1Exception):
    """Raised when the server returns a 400 Bad Request response."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        super().__init__(error_code, message)


class TributeApiV1Unauthorized(TributeApiV1Exception):
    """Raised when the server returns a 401 Unauthorized response."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        super().__init__(error_code, message)


class TributeApiV1Forbidden(TributeApiV1Exception):
    """Raised when the server returns a 403 Forbidden response."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        super().__init__(error_code, message)


class TributeApiV1NotFound(TributeApiV1Exception):
    """Raised when the server returns a 404 Not Found response."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        super().__init__(error_code, message)


class TributeApiV1Conflict(TributeApiV1Exception):
    """Raised when the server returns a 409 Conflict response."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        super().__init__(error_code, message)


class TributeApiV1TooManyRequests(TributeApiV1Exception):
    """Raised when the server returns a 429 Too Many Requests response."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        super().__init__(error_code, message)


class TributeApiV1ServerError(TributeApiV1Exception):
    """Raised when the server returns a 500 Internal Server Error response."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        super().__init__(error_code, message)


class TributeApiV1BadGateway(TributeApiV1Exception):
    """Raised when the server returns a 502 Bad Gateway response."""

    def __init__(
        self, error_code: TributeErrorCode | None = None, message: str | None = None
    ):
        super().__init__(error_code, message)
