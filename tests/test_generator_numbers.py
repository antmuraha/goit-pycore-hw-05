import unittest
from libs.generator_numbers import generator_numbers, sum_profit


class TestGeneratorNumbers(unittest.TestCase):
    def test_generator_numbers(self):
        text = "The total 123.45x 123.456 .456 123. income of the employee consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
        numbers = generator_numbers(text)
        total_income = sum_profit(numbers)

        self.assertEqual(total_income, 1351.46)


if __name__ == '__main__':
    unittest.main()
