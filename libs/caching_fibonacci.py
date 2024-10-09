from collections.abc import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """A function that calculates Fibonacci numbers using caching from previous calls"""

    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0

        if n == 1:
            return 1

        cache_value = cache.get(n)
        if cache_value:
            # print(n, cache_value)
            return cache_value

        cache_value = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = cache_value
        return cache_value

    return fibonacci
