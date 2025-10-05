import pytest

from src.conditional_execution import (
    check_pass_fail,
    get_age_group,
    safe_to_int,
    safe_divide,
)


def test_check_pass_fail() -> None:
    assert check_pass_fail(75) == "pass"
    assert check_pass_fail(60) == "pass"
    assert check_pass_fail(59) == "fail"
    assert check_pass_fail(51, 50) == "pass"
    assert check_pass_fail(99, 100) == "fail"
    assert check_pass_fail(-1 , 0) == "fail"


def test_get_age_group() -> None:
    assert get_age_group(10) == "child"
    assert get_age_group(13) == "teenager"
    assert get_age_group(18) == "teenager"
    assert get_age_group(20) == "adult"


def test_safe_to_int() -> None:
    assert safe_to_int("42") == 42
    assert safe_to_int(42.0) == 42
    assert safe_to_int("hello") == 0
    assert safe_to_int(4 + 2j) == 0


def test_safe_divide() -> None:
    assert safe_divide(12, 3) == 4.0
    assert safe_divide(12, 0) == 0.0
    assert safe_divide(12, 0.0) == 0.0
    with pytest.raises(Exception):
        safe_divide(12, "hello") == 0.0
