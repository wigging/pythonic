---
title: Textwrap dedent
permalink: textwrapdedent
---

Remove leading whitespace from every line in text with the `textwrap.dedent()` function. The first example prints the leading white space in the string which is caused by the indentation of the function. The second example uses `textwrap.dedent()` to remove the leading white space.

```python
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


>>> print_ex1()
    This is a long line
    of words.

>>> print_ex2()
This is a long line
of words.
```
