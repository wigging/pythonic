"""Example of importlib and getattr.

The importlib is used for package import while the getattr is used for class
or function resolution. Run this example with `uv run example.py`.
"""

import importlib


def main():
    """Run the example."""

    # Import the entire package
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


if __name__ == "__main__":
    main()
