---
title: Debugger in Python
date: July 18, 2023
---

The [pdb](https://docs.python.org/3/library/pdb.html) module provides an interactive debugger for Python programs. It supports breakpoints and stepping through the source code. To demonstrate using the debugger and setting a breakpoint, first consider the example shown below.

```python
def main():
    """
    Iterate through a range of numbers, double the number, and determine if
    the number is divisible by 3.
    """

    for number in range(10):

        number_x2 = number * 2

        print('number   is', number)
        print('number×2 is', number_x2)

        if number != 0 and number % 3 == 0:
            print('number is divisible by 3')


if __name__ == '__main__':
    main()

```

```text
number   is 0
number×2 is 0
number   is 1
number×2 is 2
number   is 2
number×2 is 4
number   is 3
number×2 is 6
number is divisible by 3
number   is 4
number×2 is 8
number   is 5
number×2 is 10
number   is 6
number×2 is 12
number is divisible by 3
number   is 7
number×2 is 14
number   is 8
number×2 is 16
number   is 9
number×2 is 18
number is divisible by 3
```

## Using pdb and set_trace()

Import `pdb` then call `pdb.set_trace()` at the location where you want to break into the debugger as shown in the code below. The `(Pdb)` is the debugger's prompt which indicates you are in debug mode. While in debug mode, you can inspect variables and perform actions such as move to the next line with `n` or continue execution with `c`. Enter `q` to quit debug mode.

```python
import pdb


def main():
    """
    Set trace if number divisible by 3.
    """

    for number in range(10):

        number_x2 = number * 2

        print('number   is', number)
        print('number×2 is', number_x2)

        if number != 0 and number % 3 == 0:
            pdb.set_trace()
            print('number is divisible by 3')


if __name__ == '__main__':
    main()
```

```text
number   is 0
number×2 is 0
number   is 1
number×2 is 2
number   is 2
number×2 is 4
number   is 3
number×2 is 6
> /Desktop/pythonic/python-projects/debugger/pdb_example.py(18)main()
-> print('number is divisible by 3')
(Pdb) number_x2
6
```

## Using breakpoint()

The `breakpoint()` function introduced in Python 3.7 can be used instead of the `import pdb; pdb.set_trace()` as shown in the next example.

```python
def main():
    """
    Call breakpoint if number divisible by 3.
    """

    for number in range(10):

        number_x2 = number * 2

        print('number   is', number)
        print('number×2 is', number_x2)

        if number != 0 and number % 3 == 0:
            breakpoint()
            print('number is divisible by 3')


if __name__ == '__main__':
    main()
```

```text
number   is 0
number×2 is 0
number   is 1
number×2 is 2
number   is 2
number×2 is 4
number   is 3
number×2 is 6
> /Desktop/pythonic/python-projects/debugger/breakpoint_example.py(16)main()
     15             breakpoint()
---> 16             print('number is divisible by 3')
     17

ipdb>
```

Notice the debug prompt `ipdb>` for this example looks different than the debug prompt for the previous example. The advantage of using `breakpoint()` is that it can call other debuggers by setting the `PYTHONBREAKPOINT` environment variable. In this example, the [ipdb](https://github.com/gotcha/ipdb) debugger is used because it is defined in the `.zshrc` file as shown below.

```text
# Use ipdb as the Python breakpoint() debugger
export PYTHONBREAKPOINT=ipdb.set_trace
```
