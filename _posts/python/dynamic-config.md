---
title: Dynamic Python Class from TOML
date: April 21, 2025
---

Python's standard library provides functionality to read a TOML configuration file and dynamically create class instances based on the parameters defined in that file. This is useful for command line tools and web applications.

## Package

Suppose we have a package named benchmarks as shown below. This package provides several classes that can be created from parameters defined in a TOML file. The content of each file in the package is also shown below.

```text
benchmarks/
├── __init__.py
├── alpha.py
├── bravo.py
├── charlie.py
└── roger.py
```

```python
# __init__.py

from .alpha import Alpha
from .bravo import Bravo
from .charlie import Charlie
from .roger import Roger

__all__ = ["Alpha", "Bravo", "Charlie", "Roger"]

# alpha.py

class Alpha:
    def __init__(self):
        self.name = "Alpha"

# bravo.py

class Bravo:
    def __init__(self, weight, age):
        self.name = "Bravo"
        self.weight = weight
        self.age = age

# charlie.py

class Charlie:
    def __init__(self, weight=12.2, age=90):
        self.name = "Charlie"
        self.weight = weight
        self.age = age

# roger.py

class Roger:
    def __init__(self, weight):
        self.name = "Roger"
        self.weight = weight
```

## TOML file

The TOML file shown here provides configuration parameters for the classes in the benchmarks package. The `name` identifies which class to use for the parameters in that benchmark.

```toml
title = "Config for benchmarks"

[[benchmark]]
name = "alpha"

[[benchmark]]
name = "bravo"
weight = 23.1
age = 89

[[benchmark]]
name = "roger"
weight = 14.95

[[benchmark]]
name = "charlie"
```

## Example

In the Python code shown below, the configuration is loaded from the TOML file using Python's `tomllib` module. Next, the class object for each benchmark is obtained using the `name` value from the TOML config and the `getattr` function. The `inspect` module gets the input parameters needed for the class which are used to create a dictionary of input values. The dictionary is then used to create a class instance.

```python
# main.py

import inspect
import tomllib
import benchmarks


def main():
    """Run this example."""

    # Get configuration from TOML file
    with open("config.toml", "rb") as f:
        data = tomllib.load(f)

    for config in data["benchmark"]:
        # Get the class object from the package using name from TOML config file
        name = config["name"].title()
        bench_class = getattr(benchmarks, name)

        # Inspect parameters of the class constructor to get applicable
        # inputs. Then build dictionary of input parameters using values
        # defined in TOML config file.
        sig = inspect.signature(bench_class)
        kwargs = {k: config[k] for k in sig.parameters if k in config}

        # Create the class instance with the matched args
        b = bench_class(**kwargs)

        print(b)
        print(vars(b), "\n")


if __name__ == "__main__":
    main()
```

Below is the print output from running this example.

```text
<benchmarks.alpha.Alpha object at 0x100665550>
{'name': 'Alpha'}

<benchmarks.bravo.Bravo object at 0x1006656a0>
{'name': 'Bravo', 'weight': 23.1, 'age': 89}

<benchmarks.roger.Roger object at 0x100665550>
{'name': 'Roger', 'weight': 14.95}

<benchmarks.charlie.Charlie object at 0x1006656a0>
{'name': 'Charlie', 'weight': 12.2, 'age': 90}
```

The example code and package are available in the pythonic repo on GitHub at [pythonic/projects/dynamic-config](https://github.com/wigging/pythonic/tree/main/projects/dynamic-config).

## Further reading

See the [tomllib](https://docs.python.org/3/library/importlib.html), [getattr](https://docs.python.org/3/library/functions.html#getattr), and [inspect](https://docs.python.org/3/library/inspect.html) documentation for more details. More information about the TOML spec is available at <https://toml.io>.