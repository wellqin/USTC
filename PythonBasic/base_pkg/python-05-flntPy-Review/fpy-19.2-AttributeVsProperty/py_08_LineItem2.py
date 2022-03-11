"""
    tests of LineItem class
    >>> raisins = LineItem('Golden raisins', 10, 6.95)
    >>> raisins.subtotal()
    69.5
    >>> walnust = LineItem('walnuts', 0, 10.00)
    Traceback (most recent call last):
        ...
    ValueError: value must be > 0
"""


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight      = weight
        self.price       = price

    def subtotal(self):
        return self.weight * self.price
    
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')

if __name__ == "__main__":
    import doctest
    doctest.testmod()