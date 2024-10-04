import uuid
for i in range(3):
    """
    Because of the time component, 
    each call to uuid1() returns a new value.

    In this output, only the time component 
    (at the beginning of the string) changes.
    """
    print(uuid.uuid1())
    