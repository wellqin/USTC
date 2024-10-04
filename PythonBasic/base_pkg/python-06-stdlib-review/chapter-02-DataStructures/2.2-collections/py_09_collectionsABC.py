"""
Table of Abstract Base Classes

+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| class           | Base class(es)              | API Purpose                                                                           |
+=================+=============================+=======================================================================================+
| Container       |                             | Basic container features, such as the *in* operator                                   |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Hashable        |                             | Adds support for providing a hash value for container instances                       |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Iterable        |                             | Can create an interator over the container contents                                   |                  
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Iterator        | Iterable                    | Is an iterator over the container contents                                            |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Generator       | Iterator                    | Extends iterators with the generator protocol                                         |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Sized           |                             | Adds methods for containers that know how big they are                                |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Callable        |                             | For containers that can be invoked as a function                                      |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Sequence        | Sized, Iterable, Container  | Supports retrieving individual items, iterating, and changing the order of items      |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| MutableSequence | Sequence                    | Supports adding and removing items to an instance after it has been created           |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| ByteString      | Sequence                    | Combined API of bytes amd bytearray                                                   |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Set             | Sized, Iterable, Container  | Supports set operations such as intersection and union                                |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| MutableSet      | Set                         | Adds methods for manipulating the set contents after it is created                    |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Mapping         | Sized, Iterable, Container  | Defines the read-only API used by dict                                                |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| MutableMapping  | Mapping                     | Defines the methods for manipulating the contents of a mapping after created          |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| MappingView     | Sized                       | Defines the view API for accessing a mapping from an iterator                         |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| ItemsView       | MappingView, Set            | Part of the view API                                                                  |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| KeysView        | MappingView, Set            | Part of the view API                                                                  |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| ValueView       | MappingView                 | Part of the view API                                                                  |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Awaitable       |                             | API for objects that can be used in await expression, such as coroutines              |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| Coroutine       | Awaitable                   | API for classes that implement the coroutine protocol                                 |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| AsyncIterable   |                             | API for iterables compatible with async for                                           |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+
| AsyncIterator   | AsyncIterable               | API for asynchronous iterators                                                        |
+-----------------+-----------------------------+---------------------------------------------------------------------------------------+

"""

import collections, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

def main():
    pass

if __name__ == "__main__":
    main()