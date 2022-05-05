import unittest

from typing import Union

from function import convert_fahrenheit_to_celsius


class TestFahrenheitConversion(unittest.TestCase):
	"""Class that contains tests for fahrenheit conversion."""

	KELVIN_CONSTANT = 273.15


	def reaumur_to_celsius(self, reaumur: Union[float, int]) -> float:
		"""Converts temperature from fahrenheit to celsius

		:param reaumur: Temperature in reaumur scale.

		:returns: Temperature in celsius scale.
		"""
		return reaumur/0.8


	def test_if_fahrenheit_to_celsius_is_correct(self) -> None:
		"""Test if the conversion from fahrenheit to celsius is correct."""

		for fahrenheit, expected in zip([50, 60, 90], [10, 15, 32]):
			self.assertEqual(
				int(convert_fahrenheit_to_celsius(fahrenheit)),
				expected
			)

	def test_function_do_not_return_correct_value_for_reaumur_scale(self) -> None:
		"""Test if the function raises from fahrenheit to celsius is correct."""

		for reaumur, expected in zip([50, 60, 90], [10, 15, 32]):
			self.assertNotEqual(
				int(self.reaumur_to_celsius(reaumur)),
				expected
			)

	def test_if_fahrenheit_to_kelvin_is_correct(self) -> None:
		for fahrenheit, expected in zip([50, 60, 90], [283.15, 288.15, 305.15]):
			self.assertEqual(
				int(convert_fahrenheit_to_celsius(fahrenheit)) + self.KELVIN_CONSTANT,
				expected
			)
