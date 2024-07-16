from typing import Any


class BaseError(Exception):
    def __init__(
        self, *_: tuple[Any], message: str = ""
    ) -> None:
        self.message = message
        super().__init__(message)


class EmptyValueError(BaseError):
    def __init__(
        self, *_: tuple[Any], value: str,
    ) -> None:
        self.message = f"Value cannot be empty: {value}"
        super().__init__(message=self.message)


class InvalidTextLengthError(BaseError):
    def __init__(
            self, *_: tuple[Any], value: str
    ) -> None:
        self.message = f"Value '{value}' must be of valid length (not too short or too long)."
        super().__init__(message= self.message)
