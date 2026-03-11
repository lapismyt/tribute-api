from typing import NoReturn
from uuid import UUID

from tribute_api._types import AnyUUID
from tribute_api.v1.exceptions import (
    TributeApiV1BadGateway,
    TributeApiV1BadRequest,
    TributeApiV1Conflict,
    TributeApiV1Exception,
    TributeApiV1Forbidden,
    TributeApiV1NotFound,
    TributeApiV1ServerError,
    TributeApiV1TooManyRequests,
    TributeApiV1Unauthorized,
)
from tribute_api.v1.models._error import TributeError


def uuid_to_str(uuid: AnyUUID) -> str:
    if isinstance(uuid, UUID):
        return str(uuid)
    return uuid


def raise_from_error_tuple(err_tup: tuple[int, TributeError]) -> NoReturn:
    """Raises a TributeApiV1Exception from an error tuple returned by the raw client.

    Args:
        err_tup (tuple[int, TributeError]): Error tuple returned by the raw client.

    Raises:
        TributeApiV1BadRequest: If status code is 400 (Bad Request).
        TributeApiV1Unauthorized: If status code is 401 (Unauthorized).
        TributeApiV1Forbidden: If status code is 403 (Forbidden).
        TributeApiV1NotFound: If status code is 404 (Not Found).
        TributeApiV1Conflict: If status code is 409 (Conflict).
        TributeApiV1TooManyRequests: If status code is 429 (Too Many Requests).
        TributeApiV1ServerError: If status code is 500 (Internal Server Error).
        TributeApiV1BadGateway: If status code is 502 (Bad Gateway).
        TributeApiV1Exception: If status code is not handled by a specific exception.
    """

    status, error = err_tup

    match status:
        case 400:
            raise TributeApiV1BadRequest(error.code, error.message)
        case 401:
            raise TributeApiV1Unauthorized(error.code, error.message)
        case 403:
            raise TributeApiV1Forbidden(error.code, error.message)
        case 404:
            raise TributeApiV1NotFound(error.code, error.message)
        case 409:
            raise TributeApiV1Conflict(error.code, error.message)
        case 429:
            raise TributeApiV1TooManyRequests(error.code, error.message)
        case 500:
            raise TributeApiV1ServerError(error.code, error.message)
        case 502:
            raise TributeApiV1BadGateway(error.code, error.message)
        case _:
            raise TributeApiV1Exception(error.code, error.message)
