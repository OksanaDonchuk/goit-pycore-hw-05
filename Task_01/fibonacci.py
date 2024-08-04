from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    Creates a Fibonacci function with caching to store and reuse previously computed values.
    
    :return: A function that computes the n-th Fibonacci number with caching.
    """
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Computes the n-th Fibonacci number using recursion and caching.

        :param n: The position in the Fibonacci sequence to compute.
        :return: The n-th Fibonacci number.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci


if __name__ == "__main__":
    
    fib = caching_fibonacci()
    