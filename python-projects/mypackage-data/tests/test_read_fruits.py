from mypackage import read_fruits

OUTPUT = """File path is
/opt/miniconda3/envs/myenv/lib/python3.10/site-packages/mypackage/data/fruits.csv
Pandas dataframe is
      name   quantity   price
0   apples          3    2.50
1   lemons          1    0.45
2  bananas          6    3.99
"""


def test_fruit_reader(capfd):
    read_fruits()
    out, _ = capfd.readouterr()
    assert out == OUTPUT
