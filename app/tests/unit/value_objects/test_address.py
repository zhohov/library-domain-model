import pytest
from src.domain.value_objects import Address
from src.exceptions import EmptyValueError, InvalidTextLengthError


def test_successful_create_address() -> None:
    address = Address(city="Moscow", street="Arbat", postcode="119019")

    assert address.city == "Moscow"
    assert address.street == "Arbat"
    assert address.postcode == "119019"


def test_addresses_equals() -> None:
    address1 = Address(city="Moscow", street="Arbat", postcode="119019")
    address2 = Address(city="Moscow", street="Arbat", postcode="119019")

    assert address1 == address2


class TestEmptyValidate:
    def test_create_address_with_empty_city(self) -> None:
        with pytest.raises(EmptyValueError) as exc:
            Address(city="", street="Arbat", postcode="119019")
        assert str(exc.value) == "Value cannot be empty: city"


    def test_create_address_with_empty_street(self) -> None:
        with pytest.raises(EmptyValueError) as exc:
            Address(city="Moscow", street="", postcode="119019")
        assert str(exc.value) == "Value cannot be empty: street"


    def test_create_address_with_empty_postcode(self) -> None:
        with pytest.raises(EmptyValueError) as exc:
            Address(city="Moscow", street="Arbat", postcode="")
        assert str(exc.value) == "Value cannot be empty: postcode"


class TestInvalidTextLengthValidate: 
    def test_create_address_with_invalid_value_city(self) -> None:
        with pytest.raises(InvalidTextLengthError) as exc:
            Address(city="Mo", street="Arbat", postcode="119019")
        assert str(exc.value) == "Value 'city' must be of valid length (not too short or too long)."


    def test_create_address_with_invalid_value_street(self) -> None:
        with pytest.raises(InvalidTextLengthError) as exc:
            Address(city="Moscow", street="Ar", postcode="119019")
        assert str(exc.value) == "Value 'street' must be of valid length (not too short or too long)."


    def test_create_address_with_invalid_value_postcode(self) -> None:
        with pytest.raises(InvalidTextLengthError) as exc:
            Address(city="Moscow", street="Arbat", postcode="11")
        assert str(exc.value) == "Value 'postcode' must be of valid length (not too short or too long)."
    

