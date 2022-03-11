"""
    tests of LineItem class
    >>> raisins = LineItem('Golden raisins', 10, 6.95)
    >>> raisins.subtotal()
    69.5
    >>> raisins.weight = -20
    Traceback (most recent call last):
        ...
    ValueError: Value must be > 0
"""


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight      = weight
        self.price       = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('Value must be > 0')
    # property(fget=None, fset=None, fdel=None, doc=None) is a typical approach.
    # @property is decoracto
    weight = property(get_weight, set_weight)

if __name__ == "__main__":
    import doctest
    doctest.testmod()