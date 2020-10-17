from functools import lru_cache


@lru_cache
def cached_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return cached_fib(n - 1) + cached_fib(n - 2)
