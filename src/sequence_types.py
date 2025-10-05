from copy import copy

def get_by_position(in_list: list, pos: int) -> any:
    """
    Returns an item from a list based on its position.

    Example: 
        Given fruits = ["apple", "banana", "orange"]
        get_by_position(fruits, 1) returns "banana"

    Parameters:
        in_list (list): The list to return an item from

    Returns:
        any: The element found at the given position.
    """
    pass


def get_sublist(in_list: list, start_idx: int, end_idx: int) -> list:
    """
    Returns a sublist, from the start up to but not including the end position.

    Example:
        Given vegetables = ["cucumber", "tomato", "leek", "peas", "onions"]
        get_sublist(vegetables, 1, 3) returns ["tomato", "leek"]

    Parameters:
        in_list (list): The list to return a sublist from
        start_idx (int): The index of in_list the sublist starts from
        end_idx (int): The index of in_list the sublists ends at

    Returns:
        list: The sublist from the start up to but not icluding the end
    """
    pass


def get_every_other_element(original_list: list) -> list:
    """
    Returns a new list that contains every other element from the original list, 
    beginning with the first.

    Example:
        [0, 1, 2, 3, 4, 5] -> [0, 2, 4]

    Parameters:
        original_list (list): The original list to parse.

    Returns:
        list: A new list containing every other element.
    """
    pass


def reverse_string(text: str) -> str:
    """
    Reverses a string sequence.

    Example:
        reverse_string("hello") returns "olleh"

    Parameters:
        text (str): The string to reverse

    Returns:
        str: The reversed string
    """
    pass


def replace_at(in_list: list, idx: int, new_value: any) -> None:
    """
    Replaces a list element at a given position by a new element. 
    The list is modified in place.

    Example:
        Given shopping = ["cheese", "beer", "chocolate"]
        replace_at(shopping, 1, "water") changes shopping to ["cheese", "water", "chocolate"]

    Returns:
        None (in_list is modified in place)
    """
    pass


def insert_at_position(in_list: list, value: any, pos: int = -1) -> None:
    """
    Inserts a new value at a position in a list. If no position is given, inserts at the end.

    Example: 
        Given shopping = ["bread", "butter", "ham"]
        insert_at_position(shopping, "cheese") changes shopping to ["bread", "butter", "ham", "cheese"]
        insert_at_position(shopping, "cheese", 2) changes shopping to ["bread", "butter", "cheerse", "ham"]

    Hint:
        Create a list and bind it to a variable, then type 'variable.' in your IDE. Use the context menu to
        explore what operations are allowed on the list.

    Parameters:
        in_list(list): The list to modify.
        value(any): The new value to insert to the list.
        pos(int, optional): The index at which to insert the value.

    Returns:
        None (in_list is modified in place)
    """
    pass
    

# -- Do not modify code below this line
def main() -> None:
    sample_list = ["bread", "butter", "ham"]
    print(f"Sample list: {sample_list}")

    print(f"Get by position (position 1): {get_by_position(sample_list, 1)}")
    print(f"Get sublist (1-2): {get_sublist(sample_list, 1, 2)}")
    print(f"Get every other element: {get_every_other_element(sample_list)}")
    print(f"Reversed string: {reverse_string(sample_list[1])}")

    list_for_replacement = sample_list.copy()
    replace_at(list_for_replacement, 2, 'cheese')
    print(f"Replace at (position 2): {list_for_replacement}")

    list_for_insertion = sample_list.copy()
    insert_at_position(list_for_insertion, 'cheese', 2)
    print(f"Insert at (position 2): {list_for_insertion}")


if __name__ == "__main__":
    main()
