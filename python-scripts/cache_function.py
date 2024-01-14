"""
Example of using cache with a function.
"""

import time
from functools import cache


def coeffs_one(method):
    """
    Get the a and b coefficients for a given method.
    """
    time.sleep(2)

    if method == "yaws":
        a, b = 1, 2
    elif method == "graham":
        a, b = 2, 4
    else:
        a, b = 0, 0

    return a, b


@cache
def coeffs_two(method):
    """
    Get the a and b coefficients for a given method.
    """
    time.sleep(2)

    if method == "yaws":
        a, b = 1, 2
    elif method == "graham":
        a, b = 2, 4
    else:
        a, b = 0, 0

    return a, b


def run_example1():
    """
    Run example using coeffs_one with no cache.
    """
    print("\nExample 1 no function cache")

    for _ in range(3):
        ti = time.perf_counter()
        a, b = coeffs_one("graham")
        tf = time.perf_counter()
        print(f"a is {a} | b is {b} | Elapsed {tf - ti:.4f} s")


def run_example2():
    """
    Run example using coeffs_two with cache.
    """
    print("\nExample 2 with function cache")

    for _ in range(3):
        ti = time.perf_counter()
        a, b = coeffs_two("graham")
        tf = time.perf_counter()
        print(f"a is {a} | b is {b} | Elapsed {tf - ti:.4f} s")


if __name__ == "__main__":
    run_example1()
    run_example2()
