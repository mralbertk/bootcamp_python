from typing import Sequence

def count_uniques(seq: Sequence) -> int:
    """
    Count the number of unique elements in a sequence.

    Example:
        Given my_list = [0, 0, 1, 2, 3]
        Given my_tuple = (0, 1, 2, 3, 4)
        count_uniques(my_list) returns 4
        count_uniques(my_tuple) returns 5

    Parameters:
        seq(Sequence): My sequence to check for unique items

    Returns:
        int: The number of unique items in the sequence
    """
    pass


def contains_duplicates(l: list) -> bool:
    """
    Checks if a list contains duplicates.

    Example:
        Given no_duplicates = ["apples", "bananas", "oranges"]
        Given with_duplicates = ["apples", "bananas", "bananas"]
        contains_duplicates(no_duplicates) returns False
        contains_duplicates(with_duplicates) returns True

    Parameters:
        l(list): The list to check for duplicates

    Returns:
        bool: True if the list contains duplicates, otherwise False
    """
    pass


def find_duplicates(l: list) -> set:
    """
    Checks if a list contains duplicates and returns them.

    Example:
        Given no_duplicates = ["apples", "bananas", "oranges"]
        Given with_duplicates = ["apples", "bananas", "bananas"]
        find_duplicates(no_duplicates) returns an empty set
        find_duplicates(with_duplicates) returns {"bananas"}

    Parameters:
        l(list): The list to check for duplicates

    Returns:
        set: The duplicate items found in the list. May be empty.
    """
    pass


def count_duplicates(l: list) -> dict:
    """
    Checks if a list contains duplicates and returns how often each occurs.

    Example:
        Given no_duplicates = ["apples", "bananas", "oranges"]
        Given with_duplicates = ["apples", "bananas", "bananas"]
        count_duplicates(no_duplicates) returns an empty dictionary
        count_duplicates(with_duplicates) returns {"bananas": 2}

    Hint:
        You may find this unnecessarily complicated. That's because it is.
        
        Start by counting how often each element occurs.

    Parameters:
        l(list): The list to check for duplicates

    Returns:
        dict: A dictionary containing all duplicates and how often they occur.
    """
    pass


def main() -> None:
    """Use this function to run and test your work.
    
    Example:
        result = count_uniques([1, 1, 2])   # You would expect this to return 2
        print(result)                       # You would expect this to print 2
    """
    pass


# -- Do not modify code below this line
if __name__ == "__main__":
    main()
