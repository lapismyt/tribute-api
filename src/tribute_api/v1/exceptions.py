from tribute_api.v1.enums import TributeErrorCode


class TributeApiV1Error(Exception):
    def __init__(self, error_code: TributeErrorCode, message: str):
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return f"{self.error_code}: {self.message}"
