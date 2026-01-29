"""Compare lookup speed for a set and list."""

import time
import textwrap


def list_lookup(n: int, x: int) -> float:
    """Run list lookup example."""
    big_list = list(range(n))

    tic = time.perf_counter()
    print(x in big_list)
    toc = time.perf_counter()

    return toc - tic


def set_lookup(n: int, x: int) -> float:
    """Run set lookup example."""
    big_list = list(range(n))
    big_set = set(big_list)

    tic = time.perf_counter()
    print(x in big_set)
    toc = time.perf_counter()

    return toc - tic


def main():
    """Run examples."""

    n = 2_000_000  # size of set or list
    x = 99_999  # value to lookup

    t_list = list_lookup(n, x)
    t_set = set_lookup(n, x)

    results = f"""
    n = {n:,}
    x = {x:,}
    List lookup: {t_list:.8f} s
    Set lookup:  {t_set:.8f} s
    Set speedup: {t_list / t_set:.1f}x
    """
    print(textwrap.dedent(results))


if __name__ == "__main__":
    main()
