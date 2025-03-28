---
title: Unittest CSV Files with Python
date: November 8, 2022
---

The example below demonstrates a unit test for a function that writes data in a dictionary to CSV files.

```python
# save_to_csv.py

import numpy as np
import pathlib


def save_to_csv(output):
    """
    Save dictionary data to CSV files using the NumPy package.

    Parameters
    ----------
    output : dict
        Dictionary of data to write to CSV files. Each key is used to create a
        CSV file where the values are written to the file.

    Returns
    -------
        CSV files written to the current directory.
    """

    # Create path for saving files
    path = pathlib.Path('.')
    path.mkdir(exist_ok=True)

    # Save simulation output to CSV files
    for k, v in output.items():
        filename = k.replace(' ', '_') + '.csv'
        np.savetxt(path / filename, v, delimiter=', ')


if __name__ == '__main__':

    weights = [4, 5.2, 8, 10]
    years = np.array([[1991, 2002], [1887, 1706]])
    output = {'weights': weights, 'years': years}

    save_to_csv(output)
```

```python
# test_savetocsv.py

import numpy as np
import pathlib
import unittest
from save_to_csv import save_to_csv


class TestSaveToCsv(unittest.TestCase):

    def setUp(self):
        weights = [4, 5.2, 8, 10]
        years = np.array([[1991, 2002], [1887, 1706]])
        output = {'weights': weights, 'years': years}
        save_to_csv(output)

        self.weights = weights
        self.years = years

    def test_currents(self):
        with open('weights.csv', 'r') as f:
            weight = float(f.readline())
        self.assertEqual(self.weights[0], weight)

    def test_volts(self):
        with open('years.csv', 'r') as f:
            years = list(map(float, f.readline().split(', ')))
        self.assertEqual(self.years[0][0], years[0])

    def tearDown(self):
        path = pathlib.Path('weights.csv')
        path.unlink(missing_ok=True)

        path = pathlib.Path('years.csv')
        path.unlink(missing_ok=True)
```

In the directory containing the files, run the unit test with the following terminal command:

```bash
python -m unittest
```
