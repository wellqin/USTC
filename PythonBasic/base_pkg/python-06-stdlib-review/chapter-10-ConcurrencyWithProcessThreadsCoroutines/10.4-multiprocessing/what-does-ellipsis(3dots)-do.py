"""
Q: wtf is `...` in Python?
A: it is `Ellipsis` object. Python > 3, using `...`, Python < 3, using `Ellipsis`

Q: why the fuck do we need this?
A: for showoff? i have no funcking idea. 
   Ellipsis is just a normal object. Ellipsis itself has no special methods or properties.
   Official document says Ellipsis usually is used to expand `slice` functionality

Q: how tf do i use it?
A: see examples below

further reading: https://farer.org/2017/11/29/python-ellipsis-object/

"""
import logging, time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(threadName)s - %(message)s'
)

### example 01
def add(a: int, b: int) -> None:
    ...

### example 02
class Magic:
    def __getitem__(self, key):
        if len(key) == 3 and key[2] is Ellipsis:
            d = key[1] - key[0]
            r = key[0]
            while True:
                yield r
                r += d

def magic_thing():
    ap = Magic()
    for i in ap[1, 3, ...]:
        logging.debug(f'{i}') # ! infinite loop
        time.sleep(1)         # show down output

### example 03
# Numpy. yeah, i used to see it alot, but i was fucking stupid or ignorant, i did NOT care it ..
# until now. this is so fucking funny

### example 04
# PEP484 -- Type Hints. hint placeholder
from typing import Callable, Tuple
def foo() -> Callable[..., int]:
    return lambda x: 1

def bar() -> Tuple[int, ...]:
    return (1, 2, 3)

def buz() -> Tuple[int, ...]:
    return (1, 2, 3, 4)

### example 05
def treasure_against_colleague():
    a, b = 1, 0
    try:
        return a / b
    except ZeroDivisionError:
        ...

if __name__ == '__main__':
    logging.debug(f'{type(...)}')
    logging.debug(f'{bool(...)}')
    logging.debug(f'{id(...)}')
    ### normal slice object
    s = slice(1, 5, 2)
    d = list('hello world wtf is ellipsis?')
    logging.debug(d[s])
    ### magic ellipsis object
    # magic_thing()
    ### Type Hints
    logging.debug(f'{foo()}')
    logging.debug(f'{bar()}')
    logging.debug(f'{buz()}')
    ### treasure against colleague
    logging.debug(f'{treasure_against_colleague()}')