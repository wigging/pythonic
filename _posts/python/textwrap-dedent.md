---
title: Dedent Text with Python
date: February 29, 2024
---

Remove leading whitespace from every line in a string with the `textwrap.dedent()` function. The first example shown below prints a multiline string that is defined in a function. The second example prints the same string but removes the leading whitespace.

This example prints a multiline string. The string is indented on each line due to the indentation of the function body.

```python
def printer():
    s = """
    This is a really long string
    with multiple lines
    of text.
    """
    print(s)

printer()
```

The output is shown below. Notice the output includes the indentation from the string.

```text
    This is a really long string
    with multiple lines
    of text.
```

This example uses the `textwrap.dedent()` function to remove the leading whitespace from every line in the string.

```python
from textwrap import dedent

def printer():
    s = """
    This is a really long string
    with multiple lines
    of text.
    """
    v = dedent(s)
    print(v)

printer()
```

The output for the dedent example is shown below. Notice the leading white space has been removed from the output.

```text
This is a really long string
with multiple lines
of text.
```
