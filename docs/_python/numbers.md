---
title: Numbers
permalink: numbers
---

Python includes three numeric types such as integers `int`, float `float`, and complex `complex` numbers.

```python
# an integer
a = 2

# a float
b = 3.89

# a complex number
c = 2 + 5j
```

## Underscore

```python
# use underscores to represent commas
>>> million = 1_000_000
>>> million
1000000
```

## Round a number

```python
# round to a whole number
>>> round(1875.82)
1876

>>> round(1875.82, -2)
1900.0

# round to a decimal place
>>> round(1875.82, 1)
1875.8
```

## Compare floats

Due to floating-point representation error, use the `isclose()` function from the math module to compare floats. Otherwise, you may get confounding results when comparing numbers.

```python
# This returns False due to floating point precision
>>> 0.1 + 0.2 == 0.3
False

# Using math.isclose() gives the expected result
>>> import math
>>> math.isclose(0.1 + 0.2, 0.3)
True
```
