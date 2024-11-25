"""Functions to read CSV files and print data."""

import pandas as pd
import importlib.resources


def read_fruits():
    """Read fruits CSV file and print data."""
    data_res = importlib.resources.files("mypackage") / "data"

    with importlib.resources.as_file(data_res / "fruits.csv") as f:
        df = pd.read_csv(f)

    print(f"\nFruits data from `fruits.csv` is below\n{df}")


def read_veggies():
    """Read veggies CSV file and print data."""
    data_res = importlib.resources.files("mypackage") / "data"

    with importlib.resources.as_file(data_res / "veggies.csv") as f:
        df = pd.read_csv(f)

    print(f"\nVeggies data from `veggies.csv` is below\n{df}")
