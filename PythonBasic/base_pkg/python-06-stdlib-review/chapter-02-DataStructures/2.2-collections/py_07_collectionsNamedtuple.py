import collections, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def collections_tuple_vs_namedtuple():
    # normal tuple. accesing elements via index
    bob  = ('Bob', 30, 'male')
    jane = tuple(['Jane', 29, 'female'])
    print('tuple, Fields by index:')
    for p in [bob, jane]:
        print('{} is a {} yo {}.'.format(*p))
    # namedtuple. also has an ability to access elements via 'label'
    # Person = collections.namedtuple('Person', ['name','age','sex']) # approach 01
    Person = collections.namedtuple('Person', 'name age sex') # approach 02
    bob    = Person('Bob', 30, 'male')
    jane   = Person('Jane', 29, 'female')
    print('\nnamedtuple, Fields by label:')
    for p in [bob, jane]:
        print('{} is a {} yo {}.'.format(*p))

@addBreaker
def collections_namedtuple_rename():
    # ? but why?
    # Python reserved keywords or repeated names are not valid in nametuple. it makes sense imright?
    # *rename* argument will auto rename labels if conflicts happen. the auto-generated names depend on index
    with_class = collections.namedtuple('Person', 'name class age', rename=True)
    print(with_class._fields)
    two_ages   = collections.namedtuple('Person', 'name age age', rename=True)
    print(two_ages._fields)

@addBreaker
def collections_namedtuple_special_attr():
    Person = collections.namedtuple('Person', 'name age')
    bob    = Person('Bob', 30)
    print('Representation   :', bob)
    print('_fields          :', bob._fields)
    print('_asdict          :', bob._asdict())
    print('_replace         :', bob._replace(name='Robert'))
    print('Representation   :', bob)

def main():
    # tuple vs namedtuple
    collections_tuple_vs_namedtuple()
    # rename
    collections_namedtuple_rename()
    # special attributes
    collections_namedtuple_special_attr()

if __name__ == "__main__":
    main()