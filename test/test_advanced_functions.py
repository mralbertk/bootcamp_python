import pytest

from src.advanced_functions import (
    factorial,
    fibonacci
)


def test_factorial() -> None:
    with pytest.raises(ValueError):
        assert factorial(-1)
    assert factorial(0) == 1
    assert factorial(7) == 5040


def test_fibonacci() -> None:
    with pytest.raises(ValueError):
        assert fibonacci(-1)
    with pytest.raises(ValueError):
        assert fibonacci(26)
    assert fibonacci(7) == 13
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
