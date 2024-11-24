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
