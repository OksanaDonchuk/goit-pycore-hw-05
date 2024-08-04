import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generates floating-point numbers found in the given text.

    :param text: The input text containing numbers.
    :return: A generator that yields floating-point numbers found in the text.
    """
    # Regular expression to find floating-point numbers
    pattern = r'\b\d+\.\d+\b'
    
    matches = re.findall(pattern, text)
    
    # Yield each number as a float
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable[[str], iter]) -> float:
    """
    Calculates the total sum of floating-point numbers found in the given text using the provided generator function.

    :param text: The input text containing numbers.
    :param func: The generator function that yields floating-point numbers.
    :return: The total sum of the numbers found in the text.
    """
    # Use the generator function to get numbers
    numbers = func(text)
    
    total_sum = sum(numbers)
    
    return total_sum


if __name__ == "__main__":
    text = "The total income of the employee consists of several parts: 1000.01 as the base income, supplemented by additional earnings of 27.45 and 324.00 dollars."
    total_income = sum_profit(text, generator_numbers)
    print(f"Total income: {total_income:.2f}")