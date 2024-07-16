from dataclasses import dataclass

from src.exceptions import EmptyValueError, InvalidTextLengthError


@dataclass(frozen=True)
class BaseValueObject:
    pass


@dataclass(frozen=True)
class Address(BaseValueObject):
    city: str
    street: str
    postcode: str

    def validate_empty_fields(self) -> None:
        if not self.city:
            raise EmptyValueError(value="city")
        if not self.street:
            raise EmptyValueError(value="street")
        if not self.postcode:
            raise EmptyValueError(value="postcode")
    
    def validate_length(self) -> None:
        if len(self.city) > 255 or len(self.city) < 3:
             raise InvalidTextLengthError(value="city")
        if len(self.street) > 255 or len(self.street) < 3:
            raise InvalidTextLengthError(value="street")
        if len(self.postcode) != 6:
            raise InvalidTextLengthError(value="postcode")

    def __post_init__(self, ) -> None:
        self.validate_empty_fields()
        self.validate_length()
