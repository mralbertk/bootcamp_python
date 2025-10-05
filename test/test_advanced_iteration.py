from src.advanced_iteration import (
    even_squares,
    name_lengths,
    convert_to_nums,
    primes_only,
)


def test_even_squares() -> None:
    _good_input = [10, 21, 32, 43, 54]
    _bad_input = ["one", "two", "three"]
    _expected_result_good_input = [100, 1024, 2916]
    _expected_result_bad_input = []
    assert even_squares(_good_input) == _expected_result_good_input
    assert even_squares(_bad_input) == _expected_result_bad_input


def test_name_lengths() -> None:
    _good_input = ["Alice", "Bob", "Charlie"]
    _bad_input = ["Alice", 3, "Charlie"]
    _expected_result_good_input = {"Alice": 5, "Bob": 3, "Charlie": 7}
    _expected_result_bad_input = {"Alice": 5, "Charlie": 7}
    assert name_lengths(_good_input) == _expected_result_good_input
    assert name_lengths(_bad_input) == _expected_result_bad_input


def test_convert_to_nums() -> None:
    _test_input = ["12.34", "17", "forty-two", "42"]
    _expected_output = [12.34, 17.0, 42.0]
    assert convert_to_nums(_test_input) == _expected_output


def test_primes_only() -> None:
    _test_input = range(100)
    _expected_output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert primes_only(_test_input) == _expected_output