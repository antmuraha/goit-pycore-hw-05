from collections.abc import Generator
import re


def generator_numbers(text: str) -> Generator[float]:
    """Selects all real numbers and returns them as a generator. Real numbers in the text are written without errors, clearly separated by spaces on both sides."""
    reg_exp = r"\s\d+\.\d{2,2}\s"

    for value in re.finditer(reg_exp, text):
        yield float(value.group().strip())


def sum_profit(numbers: Generator[float]) -> float:
    result = 0.00
    for value in numbers:
        result += value
    return result
