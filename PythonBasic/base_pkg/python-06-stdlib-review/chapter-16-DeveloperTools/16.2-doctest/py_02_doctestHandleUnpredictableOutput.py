class MyClass:
    pass

def unpredictable(obj):
    """returns a new list containing obj.
    >>> unpredictable(MyClass())
    <__main__.MyClass object at 0x...>
    """
    return obj


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import fractions