import time
from functools import cached_property


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


class Chemical2:

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


if __name__ == '__main__':

    # --- Example 1 ---

    chem = Chemical('CO2')

    for t in [25, 35.2, 45]:
        ti = time.perf_counter()
        press = chem.calc_pressure(temp=t)
        tf = time.perf_counter()

        print(f'Temp {t:5} | Press {press:,.2f} | Elapsed {tf - ti:.4f} s')

    # --- Example 2 ---

    chem = Chemical2('CO2')

    for t in [25, 35.2, 45]:
        ti = time.perf_counter()
        press = chem.calc_pressure(temp=t)
        tf = time.perf_counter()

        print(f'Temp {t:5} | Press {press:,.2f} | Elapsed {tf - ti:.4f} s')
