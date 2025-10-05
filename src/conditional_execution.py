def check_pass_fail(score: int, threshold: int = 60) -> str:
    """
    Check if an exam score results in a pass or fail grade.

    Example:
        Given score = 59
        check_pass_fail(score) returns "fail"
        check_pass_fail(score, 50) returns "pass"

    Parameters:
        score (int): The exam score
        threshold (int, optional): The minimum score for a passing grade
    
    Returns:
        str: "pass" or "fail" depending on score and threshold
    """
    pass


def get_age_group(age: int) -> str:
    """
    Returns the age group of a person based on their age.

    Age groups:
        Younger than 13: child
        13 or older: teenager
        20 or older: adult

    Example:
        Given age = 17
        get_age_group(age) returns "teenager"

    Parameters:
        age(int): The age of the person

    Returns:
        str: The age group of the person; "child", "teenager", or "adult"
    """
    pass

def safe_to_int(num: any) -> int:
    """
    Safely converts a value to an integer. Returns 0 if the value can't be converted.

    Example:
        Given my_good_number = "42"
        Given my_bad_number = "forty-two"
        safe_string_to_int(my_good_number) returns 42
        safe_string_to_int(my_bad_number) returns 0

    Parameters:
        num(any): The value to convert to integer

    Returns:
        int: Either the converted value or 0
    """
    pass


def safe_divide(numerator: float, denominator: float) -> float:
    """
    Safe division. Your program does not crash if you try to divide by 0.

    Example:
        Given good_operands: Tuple[int, int] = (12, 3)
        Given bad_operands: Tuple[int, int] = (12, 0)
        save_divide(*good_operands) returns 4.0
        save_divide(*bad_operands) returns 0.0

    Parameters:
        numerator(float): The numerator of the division operation
        denominator(float): The denominator of the vidision operation

    Hint:
        You can solve this using a try/except block or an if statement.

    Returns:
        float: The result of the division or 0.0 if a division by zero is attempted.
    """
    pass


def main() -> None:
    """Use this function to run and test your work.
    
    Example:
        result = check_pass_fail(100)   # You would expect this to return 'pass'
        print(result)                   # You would expect this to print 'pass'
    """
    pass

# -- Do not modify code below this line
if __name__ == "__main__":
    main()
