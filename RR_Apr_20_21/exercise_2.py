from typing import Union


def find_largest_fibonacci_less_than_number(n: Union[int, float]) -> int:
    """Returns the largest fibonacci less than n."""
    if n < 2:
        return 0

    previous, current, fibonacci = 0, 1, 1
    while fibonacci < n:
        previous = current
        current = fibonacci
        fibonacci = current + previous

    return fibonacci - previous


def reverse_digits(n: int) -> int:
    """Reverse the integer number and removes leading zeros.

    :param n: The number to reverse.
    :return: Reversed number.
    """
    inverted_number = ""
    for digit in reversed(str(n)):
        if digit != "0" or len(inverted_number) > 0:
            inverted_number += digit
    
    if inverted_number:
        return int(inverted_number)
    else:
        return 0
