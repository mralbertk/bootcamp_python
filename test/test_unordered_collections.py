from src.unordered_collections import (
    count_uniques,
    contains_duplicates,
    find_duplicates,
    count_duplicates,
)


def test_count_uniques() -> None:
    assert count_uniques([1, 2, 3]) == 3
    assert count_uniques([1, 1.0, 1]) == 1
    assert count_uniques(("apple", "apple", "banana")) == 2


def test_contains_duplicates() -> None:
    _no_duplicates = ["apples", "bananas", "oranges"]
    _with_duplicates = ["apples", "bananas", "bananas"]
    assert contains_duplicates(_no_duplicates) == False
    assert contains_duplicates(_with_duplicates) == True


def test_find_duplicates() -> None:
    _no_duplicates = ["apples", "bananas", "oranges"]
    _with_duplicates = ["apples", "bananas", "bananas"]
    assert find_duplicates(_no_duplicates) == set()
    assert find_duplicates(_with_duplicates) == {"bananas"}


def test_count_duplicates() -> None:
    _no_duplicates = ["apples", "bananas", "oranges"]
    _with_duplicates = ["apples", "bananas", "bananas"]
    assert count_duplicates(_no_duplicates) == {}
    assert count_duplicates(_with_duplicates) == {"bananas": 2}