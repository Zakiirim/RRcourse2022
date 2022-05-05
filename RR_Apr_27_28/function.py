from typing import Union


def convert_fahrenheit_to_celsius(fahrenheit: Union[int, float]) -> float:
	"""Converts temperature from fahrenheit to celsius

	:param fahrenheit: Temperature in fahrenheit scale.

	:returns: Temperature in celsius scale.
	"""

	return (fahrenheit-32)*(5/9)
