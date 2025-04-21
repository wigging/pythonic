---
title: Dynamic Package Import in Python
date: April 9, 2025
---

Use the `importlib` package to dynamically import a Python module by its name. Similarly, use the `getattr` function to get a class or function by name. This is useful in plugin architectures or when loading things based on configuration files.

## Package

To demonstrate, suppose we have a package named pkg as shown below. This package provides a `Fruit` class and a `say_hello` function (also shown below).

```text
pkg/
├── __init__.py
├── fruit.py
└── say_hello.py
```

```python
# pkg/__init__.py

from .fruit import Fruit
from .say_hello import say_hello

__all__ = ["Fruit", "say_hello"]
```

```python
# pkg/fruit.py

class Fruit:

    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def total(self):
        tot = self.qty * self.price
        return tot
```

```python
# pkg/say_hello.py

def say_hello(s: str):
    greeting = f"hello {s}"
    print(greeting)
```

## Example

The example given here imports the pkg package using the name of the package which is provided as a string to the `importlib.import_module`. The imported package can then be used like any other package. Next, the `getattr` function uses the name of a function or class in the package to get the corresponding object.

```python
import importlib

# Import the package and access the say_hello function
pkg = importlib.import_module("pkg")
pkg.say_hello("bart")

# Import the package and get the say_hello function
pkg = importlib.import_module("pkg")
say_hello = getattr(pkg, "say_hello")
say_hello("bart")

# Import the package and get the Fruit class
pkg = importlib.import_module("pkg")
Fruit = getattr(pkg, "Fruit")
fruit = Fruit("apple", 10, 3.58)
tot = fruit.total()
print("Total is", tot)
```

The example code and package are available in the pythonic repo on GitHub at [pythonic/projects/dynamic-import](https://github.com/wigging/pythonic/tree/main/projects/dynamic-import).

## Further reading

See the [importlib](https://docs.python.org/3/library/importlib.html) and [getattr](https://docs.python.org/3/library/functions.html#getattr) documentation for more details.