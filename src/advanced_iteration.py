from typing import Optional

def even_squares(numbers: list[int]) -> list[int]:
    """
    Parse a list of whole numbers and return a new list of the numbers squared,
    but only if the squared number is also an even number.

    If bad input is detected, the function should return an empty list.

    Example:
        Given numbers = [1, 2, 3, 4, 5, 6]
        even_squares(numbers) returns [4, 16, 36]

        Given numbers = [1, 2, "three", 4, 5, 6]
        even_squares(numbers) returns []

    Parameters:
        numbers(list): A list of whole numbers to square

    Returns:
        list: A list of squared numbers, if the squared numbers are even numbers.
    """
    pass


def name_lengths(names: list[str]) -> dict[str, int]:
    """
    Read a list of names and return a dictionary mapping each name to it's length.
    
    If a bad element is detected, it is discarded.

    Example:
        Given names = ["Alice", "Bob", "Charlie"]
        name_lenghts(names) returns {"Alice": 5, "Bob": 3, "Charlie": 7}

        Given names = ["Alice", 3, "Charlie"]
        name_lenghts(namese) returns {"Alice": 5, "Charlie": 7}
    
    Parameters:
        names(list): A list of strings

    Returns:
        dict[str, any]: A dictionary mapping each string to its length
    """
    pass


def convert_to_nums(numbers: list[str]) -> list[float]:
    """
    Converts a list of numbers in str type to a list of numbers in float type.

    Resilient to bad input; elements that cannot be converted are ignored.

    Example:
        Given numbers = ["12.34", "17", "forty-two", "42"]
        convert_to_nums returns [12.34, 17.0, 42.0]

    Hint:
        1) Use the helper function _safe_float() to convert your input.
        2) Before returning, remove 'None' objects from your output.

    Parameters:
        numbers(list): A list of strings

    Returns:
        list: A list of floats
    """
    pass


def primes_only(numbers: list[int]) -> list[int]:
    """
    Reads a list of numbers and builds a new list only inlcuding prime numbers.

    Example:
        Given my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        primes_only(my_numbers) returns [3, 5, 7]

    Hint:
        Define the helper function _is_prime() first.
    
    Parameters:
        numbers(list): A list of numbers to process

    Returns:
        list: A list of numbers
    """
    pass


def _safe_float(object: any) -> Optional[float]:
    """
    Safely converts an object to float.

    Parameters:
        object(any): The object to convert to a float

    Returns:
        Optional[float]: The result of the conversion, either a float or None.
    """
    try:
        return float(object)
    except ValueError:
        return None


def _is_prime(num: int) -> bool:
    """
    Checks if a number is a prime number.
    
    Example:
        _is_prime(3) returns True
        _is_prime(4) returns False

    Parameters:
        num(int): A whole number

    Returns:
        bool: True if num is a prime number, else False
    """
    pass


def main() -> None:
    """Use this function to run and test your work.
    
    Example:
        result = even_squares([10, 11]) # You would expect this to return [100]
        print(result)                   # You would expect this to print [100]
    """
    pass


# -- Do not modify code below this line
if __name__ == "__main__":
    main()
