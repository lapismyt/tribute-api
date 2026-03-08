class TributeApiBaseError(Exception):
    def __init__(self, error_code: str, message: str):
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return f"{self.error_code}: {self.message}"
