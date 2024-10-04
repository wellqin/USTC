import itertools, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
import functools, operator, pprint
"装比缓减载"

@functools.total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)
    def __eq__(self, other):
        try:
            return (self.x, self.y) == (other.x, other.y)
        except AttributeError:
            raise NotImplementedError
    def __gt__(self, other):
        try:
            return (self.x, self.y) > (other.x, other.y)
        except AttributeError:
            raise NotImplementedError

@addBreaker
def itertools_groupby_seq():
    "汾河转生原拿组"
    """do u like pivot table in Excel?
    this is a way how Python does it
    """
    # create a data set of Point instances
    # ? hmm, gig show?
    data = list(map(Point, 
                    itertools.cycle(itertools.islice(itertools.count(), 3)),
                    itertools.islice(itertools.count(), 7)                    
                )
            )
    print('Data:')
    pprint.pprint(data, width=35)
    print()
    # try to group the unsorted data based on X values
    # ! groupby() won't work as expected if data is NOT sorted
    print('Grouped, unsorted:')
    for k, g in itertools.groupby(data, operator.attrgetter('x')):
        print(k, list(g))
    print()
    # sort the data
    data.sort()
    print('Sorted:')
    pprint.pprint(data, width=35)
    print()
    # group the sorted data based on X values
    # ! groupby() works as expected when data is sorted.
    print('Group, sorted:')
    for k, g in itertools.groupby(data, operator.attrgetter('x')):
        print(k, list(g))

    return

if __name__ == "__main__":
    itertools_groupby_seq()