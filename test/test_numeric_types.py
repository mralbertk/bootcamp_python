from src.numeric_types import (
    is_even,
    is_odd,
    compound_interest,
    is_valid_grade
)

def test_is_even() -> None:
    _num = 2
    assert is_even(_num) == True, f"{_num} is an even number but your function does not return True"


def test_is_odd() -> None:
    _num = 2
    assert is_odd(_num) == False, f"{_num} is not an odd number but your function does not return False"


def test_compound_interest() -> None:
    _principal = 5000
    _interest = 0.05
    _years = 5
    expected_balance = 6381

    balance = compound_interest(_principal, _interest, _years)
    assert isinstance(balance, int), f"Remember: The result must be a an integer but is {type(balance)}"
    assert balance == expected_balance, f"We expected {expected_balance} but got {balance}"


def test_is_valid_grade() -> None:

    valid_grades = [42, 100, 0]
    invalid_grades = [-1, 101]

    for grade in valid_grades:
        is_valid = is_valid_grade(grade)
        assert is_valid is True, f"{grade} is valid but your function returned False"

    for grade in invalid_grades:
        is_valid = is_valid_grade(grade)
        assert is_valid is False, f"{grade} is not valid but your function returned True"
