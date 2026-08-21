def square_of_sum(number: int) -> int:
    """Calculate the square of the sum of numbers up to the given number.

Args:
    number (int): The upper limit of the range (inclusive).

Returns:
    int: The square of the sum of numbers from 1 to number.
"""
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """Calculate the sum of the squares of numbers up to the given number.

Args:
    number (int): The upper limit of the range (inclusive).

Returns:
    int: The sum of each number squared from 1 to number.
"""
    return sum(i ** 2 for i in range(1, number + 1))


def difference_of_squares(number: int) -> int:
    """Calculate the difference between square of sum and sum of squares.

Args:
    number (int): The upper limit of the range (inclusive).

Returns:
    int: The difference between square_of_sum and sum_of_squares.
"""
    return square_of_sum(number) - sum_of_squares(number)