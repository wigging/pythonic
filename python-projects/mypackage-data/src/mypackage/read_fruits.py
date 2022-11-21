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
