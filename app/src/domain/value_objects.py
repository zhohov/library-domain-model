from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject:
    pass


@dataclass(frozen=True)
class Address(BaseValueObject):
    city: str
    street: str
    postcode: str

    def __post_init__(self, ) -> None:
        if not self.city:
            raise ValueError("City cannot be empty")

