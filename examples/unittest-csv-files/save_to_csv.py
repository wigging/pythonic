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
