"""Module with a class."""


class Fruit:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def total(self):
        tot = self.qty * self.price
        return tot
