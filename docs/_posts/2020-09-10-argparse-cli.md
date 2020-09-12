---
title: Argparse command-line interface
category: commandline
---

The `argparse` module provides an interface to write command-line programs in Python. It is the recommended command-line parsing module available in the Python standard library. An example of using `argparse` is shown below.

```python
import argparse

# arguments for the command-line parser
parser = argparse.ArgumentParser()
parser.add_argument('n', type=int, help='number of items to print')
parser.add_argument('-d', '--done', action='store_true', help='print when done')
args = parser.parse_args()

# get integer value
n = args.n
for n in range(n):
    print('Item ', n)

# get boolean value
if args.done:
    print('Program is done.')
```

The command-line program shown above is in a file named `argparse_intro.py`. Examples of running the program from the terminal are shown below:

```python
$ python argparse_intro.py 8
Item  0
Item  1
Item  2
Item  3
Item  4
Item  5
Item  6
Item  7

$ python argparse_intro.py 8 --done
Item  0
Item  1
Item  2
Item  3
Item  4
Item  5
Item  6
Item  7
Program is done.

$ python argparse_intro.py -h
usage: argparse_intro.py [-h] [-d] n

positional arguments:
  n           number of items to print

optional arguments:
  -h, --help  show this help message and exit
  -d, --done  print when done
```

## Further reading

- Argparse — Parser for Command-Line Options, Arguments and Sub-Commands. Python 3.8.6rc1 Documentation. Accessed September 10, 2020. <https://docs.python.org/3/library/argparse.html>
- Argparse Tutorial. Python 3.8.6rc1 Documentation. Accessed September 10, 2020. <https://docs.python.org/3/howto/argparse.html>
