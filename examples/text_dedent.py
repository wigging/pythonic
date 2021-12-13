"""
Remove leading whitespace from every line in text.
"""

from textwrap import dedent


def print_ex1():
    s = """
    This is a long line
    of words.
    """
    print(s)


def print_ex2():
    s = """
    This is a long line
    of words.
    """
    print(dedent(s))


if __name__ == '__main__':
    print_ex1()
    print_ex2()
