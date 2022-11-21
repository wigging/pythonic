"""
Example 2
"""

from mypackage import divider


def run_divider():
    x = 4
    y = 9.2
    d = divider(x, y)
    return d


def main():
    d = run_divider()
    print('d is', d)


if __name__ == '__main__':
    main()
