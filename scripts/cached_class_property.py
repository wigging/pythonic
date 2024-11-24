"""
Example of using a cached class property.
"""

import time
from functools import cached_property


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


def run_example1():
    """
    Run example using ChemicalOne that has no cached property.
    """
    print("\nExample 1 no cached property")

    chem = ChemicalOne("CO2")

    for t in [25, 35.2, 45]:
        ti = time.perf_counter()
        press = chem.calc_pressure(temp=t)
        tf = time.perf_counter()

        print(f"Temp {t:5} | Press {press:,.2f} | Elapsed {tf - ti:.4f} s")


def run_example2():
    """
    Run example using ChemicalTwo with cached property.
    """
    print("\nExample 2 with cached property")

    chem = ChemicalTwo("CO2")

    for t in [25, 35.2, 45]:
        ti = time.perf_counter()
        press = chem.calc_pressure(temp=t)
        tf = time.perf_counter()

        print(f"Temp {t:5} | Press {press:,.2f} | Elapsed {tf - ti:.4f} s")


if __name__ == "__main__":
    run_example1()
    run_example2()
