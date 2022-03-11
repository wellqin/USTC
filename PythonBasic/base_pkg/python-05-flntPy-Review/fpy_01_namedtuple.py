# namedtuple stores attr
import collections
Point = collections.namedtuple('Point', 'x y')
p1 = Point(1.0, 5.0)
p2 = Point(2.5, 1.5)

fmt = "(({0}-{1})**2 + ({2} - {3})**2)**(.5)"
line_length = eval(fmt.format(p1.x, p2.x, p1.y, p2.y))
print(line_length)

# namedtuple in class
from typing import NamedTuple
class ANamedTuple(NamedTuple):
    """A class stores some attrs

    :param NamedTuple: built-in NamedTuple
    :type NamedTuple: NamedTuple
    """
    foo: int
    bar: str
    baz: list

ant = ANamedTuple(1, 'bar', [])

# essential difference: allows to access elements by names or indexes

Person = collections.namedtuple("Person", 'name age sex')
# or
Person = collections.namedtuple("Person", ['name', 'age', 'sex'])
zl = Person('ZL', 35, 'male')
fmt = "name={}, age={}, sex={}"
print(fmt.format(*zl))