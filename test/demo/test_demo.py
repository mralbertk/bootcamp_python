import sys

from src.demo.demo import say_hello

def test_demo(capsys) -> None:
    say_hello()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
    assert captured.err == ""
