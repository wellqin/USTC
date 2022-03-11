"""
copy.copy()

-------------------------               a
|                       |               |
| Original container    |               |
|-----------------------|               |
|        a              |---------------|
|                       |               |
-------------------------               |
                                        |
            ↓↓↓                         |
                                        |
=========================               |
|                       |               |
|   new container       |               |
|-----------------------|               |
|       a               |---------------|
|                       |
=========================


how id() works?
https://docs.python.org/3/library/functions.html#id

id(object)
Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. 
Two objects with **non-overlapping lifetimes** may have the same id() value.

CPython implementation detail: This is the address of the object in memory.


copy.deepcopy()

-------------------------               
|                       |
| Original container    |
|-----------------------|
|        a              |---------------a
|                       |
-------------------------
                         
            ↓↓↓          
                         
=========================
|                       |
|   new container       |
|-----------------------|
|       a               |---------------a'
|                       |
=========================



"""

import copy, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from py_copy_data import MyClass

@addBreaker
def copy_shallow():
    a       = MyClass('a')
    my_list = [a]
    dup     = copy.copy(my_list)
    fmt     = '{:>25}:'
    print(fmt.format('my_list'), my_list)
    print(fmt.format('dup'), dup)
    print(fmt.format('dup is my_list'), dup is my_list)
    print(fmt.format('dup == my_list'), dup == my_list)
    print(fmt.format('dup[0] is my_list[0]'), dup[0] is my_list[0])
    print(fmt.format('dup[0] == my_list[0]'), dup[0] == my_list[0])

@addBreaker
def copy_deep():
    a       = MyClass('a')
    my_list = [a]
    dup     = copy.deepcopy(my_list)
    fmt     = '{:>25}:'
    print(fmt.format('my_list'), my_list)
    print(fmt.format('dup'), dup)
    print(fmt.format('dup is my_list'), dup is my_list)
    print(fmt.format('dup == my_list'), dup == my_list)
    print(fmt.format('dup[0] is my_list[0]'), dup[0] is my_list[0])
    print(fmt.format('dup[0] == my_list[0]'), dup[0] == my_list[0])

if __name__ == "__main__":
    # copy()
    copy_shallow()
    # deepcopy()
    copy_deep()
