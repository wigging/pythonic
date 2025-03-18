---
title: Protocols in Python
date: July 13, 2024
---

A protocol is a way to define structural typing or "duck typing" in Python. It defines a set of attributes and/or methods that an object must have in order to be considered compatible with that protocol. Below is a protocol defined as an `Activity` class which must have `name` and `duration` attributes along with a `get_message` method.

```python
from typing import Protocol

class Activity(Protocol):
    name: str
    duration: int

    def get_message(self, x: str) -> str: ...
```

Below is a `ShellActivity` class that conforms to the `Activity` protocol because it has `name` and `duration` attributes and a `get_message` method.

```python
class ShellActivity:
    name: str
    age: int
    duration: int

    def get_message(self, x: str):
        return f"hello {x}"

# Create an instance of a ShellActivity object
shell: Activity = ShellActivity()
```
