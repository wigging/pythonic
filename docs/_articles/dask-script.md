---
title: Use Dask in a script
date: 2021-11-28
---

Since most Dask examples are demonstrated using Jupyter notebooks, here's an example of using Dask in a Python file or script. Notice how the Dask code must be in the `__main__` block or called from within a function.

```python
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
```

## Example code

- [dask_script.py](https://github.com/wigging/pythonic/blob/main/examples/dask_script.py)
