---
title: Cached property
date: March 30, 2023
---

The class below sets the pressure coefficients `coeffs` based on the chemical name. In a real application, these coefficients might be read from a chemical database; therefore, getting the coefficients could take time to retrieve. This is demonstrated by the `time.sleep()` associated with the coefficients variable.

```python
import time

class Chemical:

    def __init__(self, name):
        self.name = name

    def calc_pressure(self, temp):

        if self.name == 'CO2':
            time.sleep(2)
            coeffs = [2, 5, 8.7]
        elif self.name == 'H2O':
            time.sleep(2)
            coeffs = [9, 1, 0.4]
        else:
            print('Chemical not available')
            return 0

        press = (coeffs[0] * temp) + (coeffs[1] * temp**2) + (coeffs[2] * temp**3)
        return press
```

Calculating the pressure for a range of temperatures is demonstrated below; the output is also shown. Notice the elapsed time for each loop is about 2 seconds because the coefficients are set during each iteration.

```python
chem = Chemical('CO2')

for t in [25, 35.2, 45]:
    ti = time.perf_counter()
    press = chem.calc_pressure(temp=t)
    tf = time.perf_counter()

    print(f'Temp {t:5} | Press {press:,.2f} | Elapsed {tf - ti:.4f} s')
```

```
Temp    25 | Press 139,112.50 | Elapsed 2.0032 s
Temp  35.2 | Press 385,709.21 | Elapsed 2.0051 s
Temp    45 | Press 803,002.50 | Elapsed 2.0051 s
```

Since the class instance represents a particlar chemical, the coefficients only need to be determined once. Using the `cached_property` from `functools` allows the coefficients variable `coeffs` to be a cached property of the class. This prevents the coefficients from being retrieved multiple times.

```python
import time
from functools import cached_property

class Chemical:

    def __init__(self, name):
        self.name = name

    @cached_property
    def coeffs(self):

        if self.name == 'CO2':
            time.sleep(2)
            coeff = [2, 5, 8.7]
        elif self.name == 'H2O':
            time.sleep(2)
            coeff = [9, 1, 0.4]

        return coeff

    def calc_pressure(self, temp):

        coeffs = self.coeffs
        press = (coeffs[0] * temp) + (coeffs[1] * temp**2) + (coeffs[2] * temp**3)

        return press
```

Now, calculating the pressure for a range of temperatures is significantly faster after the first iteration. Notice the elapsed time for the first loop is about 2 seconds and the remaining loops are practically zero.

```python
chem = Chemical('CO2')

for t in [25, 35.2, 45]:
    ti = time.perf_counter()
    press = chem.calc_pressure(temp=t)
    tf = time.perf_counter()

    print(f'Temp {t:5} | Press {press:,.2f} | Elapsed {tf - ti:.4f} s')
```

```
Temp    25 | Press 139,112.50 | Elapsed 2.0043 s
Temp  35.2 | Press 385,709.21 | Elapsed 0.0000 s
Temp    45 | Press 803,002.50 | Elapsed 0.0000 s
```
