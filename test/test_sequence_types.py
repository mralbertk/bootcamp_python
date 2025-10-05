from src.sequence_types import (
    get_by_position,
    get_sublist,
    get_every_other_element,
    reverse_string,
    replace_at,
    insert_at_position
)


def test_get_by_position() -> None:
    _test_list = [0, 1, 2, 3, 4, 5]
    var = get_by_position(_test_list, 2)
    assert var == 2


def test_get_sublist() -> None:
    _test_list = [0, 1, 2, 3, 4, 5]
    var = get_sublist(_test_list, 1, 4)
    assert var == [1, 2, 3]


def test_get_every_other_element() -> None:
    _test_list = [0, 1, 2, 3, 4, 5]
    var = get_every_other_element(_test_list)
    assert var == [0, 2, 4]


def test_reverse_string() -> None:
    text = "hello world"
    var = reverse_string(text)
    assert var == "dlrow olleh"


def test_replace_at() -> None:
    _test_list = [0, 1, 2, 3, 4, 5]
    replace_at(_test_list, 2, 6)
    assert _test_list == [0, 1, 6, 3, 4, 5]
 


def test_insert_at_position() -> None:
    _insert_at_default = [0, 1, 2, 3, 4, 5]
    _insert_at_position = [0, 1, 2, 3, 4, 5]
    insert_at_position(_insert_at_default, 9)
    insert_at_position(_insert_at_position, 9, 2)
    print(_insert_at_default)
    print(_insert_at_position)
    assert _insert_at_default == [0, 1, 2, 3, 4, 9, 5]
    assert _insert_at_position == [0, 1, 9, 2, 3, 4, 5]
