"""
>>> nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
>>> nutmeg.weight, nutmeg.price
(8, 13.95)
>>> sorted(vars(nutmeg).items())
[('description', 'Moluccan nutmeg'), ('price', 13.95), ('weight', 8)]
"""


def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]
    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__.update(storage_name=value)
        else:
            raise ValueError('value must be > 0')
    return property(qty_getter, qty_setter)

class LineItem:
    weight = quantity('weight') # using property factory function
    price  = quantity('price')  # using property factory function

    def __init__(self, description, weight, price):
        self.description = description
        self.weight      = weight
        self.price       = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    print(nutmeg.weight, nutmeg.price)