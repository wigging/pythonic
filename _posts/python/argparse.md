---
title: Command-line arguments with Python
date: September 28, 2024
---

The `argparse` module provides an interface to write command-line programs in Python. It is part of the Python standard library so there's no need for external dependencies. A basic example is given below that demonstrates positional and optional arguments. The second example shows the use of subparsers to create subcommands.

## Basic example

This example uses `argparse` to create positional argument `n` and an optional argument `-d`.

```python
# main.py

import argparse

# Create command-line parser and arguments
parser = argparse.ArgumentParser()
parser.add_argument('n', type=int, help='number of items to print')
parser.add_argument('-d', '--done', action='store_true', help='print when done')
args = parser.parse_args()

# Get an integer value
n = args.n
for n in range(n):
    print('Item ', n)

# Get a boolean value
if args.done:
    print('Program is done.')
```

The command-line program shown above is in a file named `main.py`. Output from running the program in the terminal are shown below.

```text
$ python main.py 8
Item  0
Item  1
Item  2
Item  3
Item  4
Item  5
Item  6
Item  7

$ python main.py 8 --done
Item  0
Item  1
Item  2
Item  3
Item  4
Item  5
Item  6
Item  7
Program is done.

$ python main.py -h
usage: main.py [-h] [-d] n

positional arguments:
  n           number of items to print

optional arguments:
  -h, --help  show this help message and exit
  -d, --done  print when done
```

## Subcommands example

This example uses subparsers to create two subcommands `start` and `stop`. Output from running the program with the subcommands is also shown below.

```python
# main.py

import argparse


def start(args):
    """Invoked by the `start` subcommand."""
    print("start it up")


def stop(args):
    """Invoked by the `stop` subcommand."""
    print("shut it down")
    if args.baz:
        print("with", args.baz)


def main():
    """Run command line parsers."""
    parser = argparse.ArgumentParser(description="Example with subparsers.")
    parser.add_argument("--num", type=int, help="number of items to print")

    subparsers = parser.add_subparsers(title="subcommands", help="valid subcommands")

    # Create subparser for `start` subcommand
    parser_start = subparsers.add_parser("start", help="start the operation")
    parser_start.set_defaults(func=start)

    # Create subparser for `stop` subcommand
    parser_b = subparsers.add_parser("stop", help="shutdown the operation")
    parser_b.set_defaults(func=stop)
    parser_b.add_argument("--baz", choices="XYZ", help="choose a letter")

    # Get command line arguments
    args = parser.parse_args()

    # Print out numbers if `num` option is given
    if args.num:
        n = args.num
        for i in range(n):
            print("item number", i)

    # Run the function associated with a subcommand
    if hasattr(args, "func"):
        args.func(args)


if __name__ == "__main__":
    main()
```

```text
$ python main.py --num 5
item number 0
item number 1
item number 2
item number 3
item number 4

$ python main.py start
start it up

$ python main.py stop
shut it down

$ python main.py stop --baz X
shut it down
with X

$ python main.py --help
usage: main.py [-h] [--num NUM] {start,stop} ...

Example with subparsers.

options:
  -h, --help    show this help message and exit
  --num NUM     number of items to print

subcommands:
  {start,stop}  valid subcommands
    start       start the operation
    stop        shutdown the operation
```
