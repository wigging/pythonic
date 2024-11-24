"""
Example of using Dask in a Python file (script) instead of in a Jupyter
notebook.
"""

import time
from distributed import Client


def adder(x):
    """
    Some function to run in parallel using Dask.
    """
    time.sleep(1)
    y = x + 1
    return y


def main():
    """
    Use the Dask distributed client to run a function in parallel.
    """
    client = Client(n_workers=8)

    numbers = [3, 4, 5, 8, 12, 18, 25]
    futures = []

    for n in numbers:
        a = client.submit(adder, n)
        futures.append(a)

    results = client.gather(futures)
    print(results)

    client.close()


if __name__ == '__main__':
    main()
