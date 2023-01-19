+++
title = "Package with data"
date = 2022-11-08
+++

The file structure below represents a Python package that includes data files. Notice the data directory is within the package at `src/mypackage/`. This source directory approach follows the conventions outlined in the [Python Packaging User Guide](https://packaging.python.org/en/latest/).

```
mypackage-data
├── README.md
├── examples
│   ├── add_numbers.py
│   └── read_fruits_data.py
├── pyproject.toml
├── src
│   └── mypackage
│       ├── __init__.py
│       ├── adder.py
│       ├── data
│       │   └── fruits.csv
│       └── read_fruits.py
└── tests
    ├── test_adder.py
    └── test_read_fruits.py
```

The `importlib.resources` module should be used to get a path to the data files. This ensures the data file's path is correct even when the package is installed on different systems.

```python
import pandas as pd
from importlib.resources import files


def read_fruits():
    """
    Read fruit data from CSV file.
    """
    path = files('mypackage') / 'data/fruits.csv'
    print(f'File path is\n{path}')

    df = pd.read_csv(path)
    print(f'Pandas dataframe is\n{df}')

```
