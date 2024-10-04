"""
! what?
Python is dynamic, interpretive lang that it not requires typing check.
But as a maniac programmers who love strong type lang such as C/C++, Java, Visual Basic etc.,
typing hint is a optional style which is supported by PEP484 

! why?
readibility matters

! how?

the built-in `typing` module is the way to go.

typing
|-- Variables
|-- Built-in types
|-- Functions
|-- When you're puzzled or when things are complicated
|-- Standard "duck types"
|-- Classes
|-- Type aliases
|-- NewType
|-- Generics
|-- UD generic types



link: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
link: https://docs.python.org/3/library/typing.html

! Python >= 3.5
"""
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s'
)

def typing_variable_hint() -> None:
    age: int = 30
    a: int #<~ ok w/o initialization 
    child: bool
    if age < 18:
        child = True
    else:
        child = False
    logging.debug(f'child: {child}')

def typing_Builtin_types() -> None:
    from typing import List, Set, Dict, Tuple, Optional
    x: int      = 1
    x: float    = 1.0
    x: bool     = True
    x: str      = "test"
    x: bytes    = b"test"
    
    x: List[int]                = [1]
    x: Set[int]                 = {6, 7}
    x: Dict[str, float]         = {'field': 2.0}
    x: Tuple[int, str, float]   = (3, 'yes', 7.5)
    x: Tuple[int, ...]          = (1, 2, 3)
    # uses Optional[] for values that could be None
    x: Optional[str]            = print()

    logging.debug(f'{x}')
    pass

def typeing_Functions() -> None:
    from typing import Callable, Iterator, Union, Optional, List
    # annotates a function definition
    def stringify(num: int) -> str:
        return str(num)
    # multiple arguments
    def plus(num1: int, num2: int) -> int:
        return num1 + num2
    # default value
    def f(num1: int, my_float: float = 3.5) -> float:
        return num1 + my_float
    
    # annotates a callable
    x: Callable[[int, float], float] = f

    # generator
    def g(n: int) -> Iterator[int]:
        i = 0
        while i < n:
            yield i
            i += 1

    # splitting annotations over several lines
    def send_email(
        address: Union[str, List[str]],
        sender: str,
        cc: Optional[List[str]],
        bcc: Optional[List[str]],
        subject: '',
        body: Optional[List[str]] = None,
    ) -> bool:
        ...
    
    # it is possible to declare the return type of a callable 
    # w/o specifying the call signature by substituting a literal ellipsis for the list of arguments in the type hint: Callable[..., ReturnType]

    # an argument can be declared position-only by giving it a name
    # starting with two underscores.
    def quux(__x: int) -> None:
        pass
    logging.debug(f'{quux(3)}')
    pass

def typing_Complicated() -> None:
    from typing import Union, Any, List, Optional, cast
    # uses Union when sth could be one of a few types. like a set
    x: List[Union[int, str]] = [3, 4, 'test', 'func']
    # uses Any if u have no idea about sth or it's too dynamic to write a type for
    x: Any
    # ambiguous args
    def call(*args: str, **kwargs: str) -> str:
        return 'result'
    # `cast` is a helper function that lets you override the inferred type of an expression.
    a = [4]
    b = cast(List[int], a)
    c = cast(List[str], a)
    logging.debug(f'{c}')

    # class
    class A:
        def __setattr__(self, name: str, value: int) -> None: ...
        def __getattr__(self, name: str) -> int: ...
    a = A()
    a.foo = 42
    a.bar = 'asyncio' # failed. but NOT runtime error
    pass

def typing_duck_types() -> None:
    from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set
    def f(ints: Iterable[int]) -> List[str]:
        return [str(x) for x in ints]
    logging.debug(f'{f(range(1, 3))}')

    def g(my_mapping: Mapping[int, str]) -> List[int]:
        my_mapping[5] = 'maybe'
        return list(my_mapping.keys())
    r = g({3:'yes', 4:'no'})
    logging.debug(f'{r}')
    """
    +----------------+---------------+--------------------+
    | diff           | Mapping       | MutableMapping     |
    +================+===============+====================+
    | dict-like ojb  | won't mutate  | might mutate       |
    +----------------+---------------+--------------------+

    """
    def h(my_mapping: MutableMapping[int, str]) -> Set[str]:
        my_mapping[5] = 'maybe'
        return set(my_mapping.values())
    r = h({3:'yes', 4:'no'})
    logging.debug(f'{r}')
    pass

def typing_class() -> None:
    class MyClass:
        # class property just acts like variable in scope
        attr: int
        charge_percent: int = 100
        # __init__ datamodel method doesnt return anything
        def __init__(self) -> None:
            ...
        # for instance methods, omit type for "self"
        def my_method(self, num: int, str1: str) -> str:
            return num * str1

    from typing import ClassVar
    class Car:
        seats: ClassVar[int] = 4    
        passengers: ClassVar[List[str]]

    from typing import List
    class Box:
        def __init__(self) -> None:
            self.items: List[str] = []

def typing_type_aliases():
    from typing import List
    Vector = List[float]

    def scale(scalar: float, vector: Vector) -> Vector:
        return [scalar * num for num in vector]
    new_vector = scale(2.0, [1.0, -4.2, 5.4])
    logging.debug(f'{new_vector}')
    pass

def tpying_new_type():
    from typing import NewType
    UserID = NewType('UserId', int)
    some_id = UserID(524313)
    logging.debug(f'{some_id}')
    pass

def typing_generics():
    from typing import TypeVar, Sequence
    T = TypeVar('T')
    def first(l: Sequence[T]) -> T:
        return l[0]
    pass

def typing_userdefined_types():
    from typing import TypeVar, Generic
    from logging import Logger
    T = TypeVar('T')
    class LoggedVar(Generic[T]):
        def __init__(self, value: T, name: str, logger: Logger) -> None:
            self.name   = name
            self.logger = logger
            self.value  = value
        def set(self, new: T) -> None:
            self.log('Set ' + repr(self.value))
            self.value = new
        def get(self) -> T:
            self.log('Get ' + repr(self.value))
            return self.value
        def log(self, message: str) -> None:
            self.logger.info('%s: %s', self.name, message)
if __name__ == "__main__":
    # variables
    typing_variable_hint()
    # built-in types
    # logging.debug('\n{:-<50}\n'.format('-')) # ugly
    typing_Builtin_types()
    # Function annotations
    typeing_Functions()
    # Complicated
    typing_Complicated()
    # list-like, dict-like, set-like etc., they are called "duck type"
    typing_duck_types()
    # type aliases
    typing_type_aliases()
    # uses the NewType() helper function to create distinct types
    tpying_new_type()