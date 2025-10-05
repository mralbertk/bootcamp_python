def factorial(num: int) -> int:
    """
    Calculate the factorial of any number. Raises a value error if the input is negative.

    Example:
        factorial(7) returns 5040
        factorial(9) returns 362880

    Parameters:
        num(int): The number to calculate the factorial for

    Returns:
        int: The factorial of num
    """
    if num < 0:
        raise ValueError(f"Input must be >=0 but was {num}")
    pass


def fibonacci(n: int) -> int:
    """
    Return the element at position n in the fibonacci sequence.

    Raises a value error 

    Reminder:
        Fibonacci-numbers are n-1 + n-2: 0, 1, 1, 2, 3, 5, 8 ...
        Sequences in computing start at 0.

    Example:
        fibonacci(7) returns the 8th element of the fibonacci sequence: 13

    Parameters:
        n(int): The element to which to compute the fibonacci sequence.

    Returns:
        int: A number of the fibonacci sequence.
    """
    if n < 0 or n > 25:
        raise ValueError(f"n must be between 0 and 25 but was {n}")
    pass


def main() -> None:
    """Use this function to run and test your work.
    
    Example:
        result = factorial(7)           # You would expect this to return 5040
        print(result)                   # You would expect this to print 5040
    """
    pass


# -- Do not modify code below this line
if __name__ == "__main__":
    main()
