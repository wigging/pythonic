---
title: Enumerations
permalink: enums
---

An enumeration is a set of symbolic names that are bound to unique, constant values. Enumerations (or enums) are implemented in Python using the `Enum` class from the `enum` module.

```python
>>> from enum import Enum

>>> class Shape(Enum):
...     Triangle = 3
...     Square = 4
...     Pentagon = 5

>>> tri = Shape.Triangle

>>> tri.name
'Triangle'

>>> tri.value
3
```
