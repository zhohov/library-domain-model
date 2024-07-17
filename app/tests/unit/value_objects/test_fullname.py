import pytest
from src.domain.value_objects import FullName
from src.exceptions import EmptyValueError


def test_successful_create_fullname() -> None:
    fullname = FullName(first_name="Ivan", last_name="Ivanov", middle_name="Ivanovich")
    
    assert fullname.first_name == "Ivan"
    assert fullname.last_name == "Ivanov"
    assert fullname.middle_name == "Ivanovich"


def test_successful_create_fullname_without_middle_name() -> None:
    fullname = FullName(first_name="Ivan", last_name="Ivanov")
    
    assert fullname.first_name == "Ivan"
    assert fullname.last_name == "Ivanov"
    assert fullname.middle_name == ""


class TestEmptyValidate:
    def test_create_address_with_empty_first_name(self) -> None:
        with pytest.raises(EmptyValueError) as exc:
            FullName(first_name="", last_name="Ivanov")
        assert str(exc.value) == "Value cannot be empty: first_name"


    def test_create_address_with_empty_last_name(self) -> None:
        with pytest.raises(EmptyValueError) as exc:
            FullName(first_name="Ivan", last_name="")
        assert str(exc.value) == "Value cannot be empty: last_name"

