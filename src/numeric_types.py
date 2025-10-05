def is_even(num: int) -> bool:
    """
    Checks if a given number is even.

    Parameters:
        num (int): The number to check

    Returns:
        bool: True if the number is even, otherwise False
    """
    pass


def is_odd(num: int) -> bool:
    """
    Checks if a given number is odd.

    Parameters:
        num (int): The number to check

    Returns:
        bool: True if the number is odd, otherwise False
    """
    pass


def is_valid_grade(grade: int) -> bool:
    """
    Checks if a grade is valid.

    A grade is considered valid if it is between 0 and 100.

    Parameters:
        grade (int): The grade to check

    Returns:
        bool: True if the grade is valid, otherwise False
    """
    pass


def compound_interest(principal: float, rate: float, years: int) -> int:
    """
    Return the account balance after n years of accumulated interest, compunded anually.

    Balance = Principal * (1 + Rate)^Years

    Parameters:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate (e.g., 0.05 for 5%).
        years (int): The number of years to accoumulate interest.

    Returns:
        float: The final balance, rounded down to the nearest integer.
    """
    pass


# -- Do not modify code below this line
def main() -> None:
    print(is_even(2))
    print(is_odd(1))
    print(is_valid_grade(42))
    print(compound_interest(100, 0.02, 10))


if __name__ == "__main__":
    main()
