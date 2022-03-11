import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class MyClass:
    pass

objects = [
    [], (), {}, 'c', 'string', b'bytes', 1, 2.3,
    MyClass, MyClass(),
]

for obj in objects:
    logging.debug('{:>10} : {}'.format(type(obj).__name__, sys.getsizeof(obj)))