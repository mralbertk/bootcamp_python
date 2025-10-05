import pytest
import src.hello as h

def test_greeting() -> None:
    message = h.make_greeting("max")
    assert message == "hello max"

def test_greeting_exception() -> None:
    with pytest.raises(TypeError):
        message = h.make_greeting(42)
