"""
Argparse module to parse command-line arguments for a Python program.
"""

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
