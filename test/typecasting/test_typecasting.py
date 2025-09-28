import pytest

import src.typecasting.typecasting as tp

def test_integer_cast() -> None:
    expected_int = tp.to_int("17")
    assert isinstance(expected_int, int)

def test_ingeger_cast_exception() -> None:
    with pytest.raises(ValueError):
        expected_exception = tp.to_int("one")

def test_float_cast() -> None:
    expected_float = tp.to_float("1.7")
    assert isinstance(expected_float, float)

def test_float_cast_exception() -> None:
    with pytest.raises(ValueError):
        expected_exception = tp.to_float("one_point_two")