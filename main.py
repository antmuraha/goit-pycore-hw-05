
from libs.caching_fibonacci import caching_fibonacci
from libs.generator_numbers import generator_numbers, sum_profit


fib = caching_fibonacci()
print(fib(10))  # Print 55
print(fib(15))  # Print 610

text = "The total income of the employee consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
numbers = generator_numbers(text)
total_income = sum_profit(numbers)
print(f"Total Income: {total_income}")
