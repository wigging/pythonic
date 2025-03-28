---
title: Cached Class Property in Python
date: January 13, 2024
---

The [functools](https://docs.python.org/3/library/functools.html) module provides a `@cached_property` decorator to store the value of a class property.

## No cached property

This example creates a class object with a single method. The method sleeps for 2 seconds to represent an expensive task. The method is called several times in the for-loop.

```python
import time


class ChemicalOne:
    def __init__(self, name):
        self.name = name

    def calc_pressure(self, temp):
        time.sleep(2)

        if self.name == "CO2":
            coeffs = [2, 5, 8.7]
        elif self.name == "H2O":
            coeffs = [9, 1, 0.4]
        else:
            coeffs = [0, 0, 0]

        press = (coeffs[0] * temp) + (coeffs[1] * temp**2) + (coeffs[2] * temp**3)
        return press


chem = ChemicalOne("CO2")

for t in [25, 35.2, 45]:
    ti = time.perf_counter()
    press = chem.calc_pressure(temp=t)
    tf = time.perf_counter()

    print(f"Temp {t:5} | Press {press:,.2f} | Elapsed {tf - ti:.4f} s")
```

The output is shown below.

```text
Temp    25 | Press 139,112.50 | Elapsed 2.0051 s
Temp  35.2 | Press 385,709.21 | Elapsed 2.0008 s
Temp    45 | Press 803,002.50 | Elapsed 2.0024 s
```

## Using cached property

This example creates a class object with a single method and uses the `@cached_property` decorator to store a property value. The property is accessed within the method.

```python
import time
from functools import cached_property


class ChemicalTwo:
    def __init__(self, name):
        self.name = name

    @cached_property
    def coeffs(self):
        time.sleep(2)

        if self.name == "CO2":
            coeff = [2, 5, 8.7]
        elif self.name == "H2O":
            coeff = [9, 1, 0.4]
        else:
            coeff = [0, 0, 0]

        return coeff

    def calc_pressure(self, temp):
        coeffs = self.coeffs
        press = (coeffs[0] * temp) + (coeffs[1] * temp**2) + (coeffs[2] * temp**3)

        return press


chem = ChemicalTwo("CO2")

for t in [25, 35.2, 45]:
    ti = time.perf_counter()
    press = chem.calc_pressure(temp=t)
    tf = time.perf_counter()

    print(f"Temp {t:5} | Press {press:,.2f} | Elapsed {tf - ti:.4f} s")
```

The output is shown below. Notice the elapsed time for the second and third runs is zero because the property used by the method is only computed once.

```text
Temp    25 | Press 139,112.50 | Elapsed 2.0005 s
Temp  35.2 | Press 385,709.21 | Elapsed 0.0000 s
Temp    45 | Press 803,002.50 | Elapsed 0.0000 s
```
