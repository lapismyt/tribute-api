from enum import StrEnum


class TributeErrorCode(StrEnum):
    BAD_REQUEST = "error_bad_request"
    NOT_FOUND = "error_not_found"
    NOT_PERMITTED = "error_not_permitted"
    NO_ACCESS = "no_access"


class TributeCurrency(StrEnum):
    EUR = "eur"
    USD = "usd"
    RUB = "rub"
