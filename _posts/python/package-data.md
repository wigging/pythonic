---
title: Python package with data
date: November 24, 2024
---

The file structure below represents a project for a Python package named `mypackage` that includes data files. The data files in this example are CSV text files located in the package's source directory at `src/mypackage/data/`. The package can be installed using `pip install .` from the root level of the project.

```text
my-project/
├── src/
│   └── mypackage/
│       ├── data/
│       │   ├── fruits.csv
│       │   └── veggies.csv
│       ├── __init__.py
│       └── reader.py
├── README.md
├── example.py
└── pyproject.toml
```

The content of the `pyproject.toml` file is shown below. Notice the data directory does not need to be explicitly stated in the pyproject file - well, at least for the hatchling build system.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mypackage"
version = "0.1"
authors = [{name = "Bart Simpson"}]
description = "A small example package"
requires-python = ">=3.10"
dependencies = ["pandas", "ruff"]
```

In the `reader.py` module are functions that read the CSV files in the data directory and print out the data. Below is a function that reads the `fruits.csv` file and prints the fruit data. Notice the use of the `importlib.resources` module to get a path to the data file. This ensures the data file's path is correct even when the package is installed on different systems.

```python
# reader.py

import pandas as pd
import importlib.resources


def read_fruits():
    """Read fruits CSV file and print data."""
    data_res = importlib.resources.files("mypackage") / "data"

    with importlib.resources.as_file(data_res / "fruits.csv") as f:
        df = pd.read_csv(f)

    print(f"\nFruits data from `fruits.csv` is below\n{df}")
```

The content of the `example.py` file is shown next. The output from running the example is also shown. The data from the CSV files is successfully read and printed out from the example script.

```python
# example.py

import mypackage as mypkg


def main():
    """Run functions from the package."""
    mypkg.read_fruits()
    mypkg.read_veggies()


if __name__ == "__main__":
    main()
```

```console
$ python example.py

Fruits data from `fruits.csv` is below
      name   quantity   price
0   apples          3    2.50
1   lemons          1    0.45
2  bananas          6    3.99

Veggies data from `veggies.csv` is below
       name   quantity   price
0   carrots          3    4.89
1  broccoli          1    1.25
2   spinach          6    2.50
3     beans         18    3.20
```

See the [Python docs](https://docs.python.org/3/library/importlib.resources.html) for more information about the `importlib.resources` module.
