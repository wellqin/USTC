import enum, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

class BugStatus(enum.Enum):
    new           = 7
    incomplete    = 6
    invalid       = 5
    wont_fix      = 4
    in_progress   = 3
    fix_committed = 2
    fix_released  = 1

    by_design     = 4
    closed        = 1

class intBugStatus(enum.IntEnum):
    """enum.IntEnum class supports its members to behave more like numbers -- aka to support comparisons
    """
    new           = 7
    incomplete    = 6
    invalid       = 5
    wont_fix      = 4
    in_progress   = 3
    fix_committed = 2
    fix_released  = 1

@enum.unique
class uniBugStatus(enum.Enum):
    new           = 7
    incomplete    = 6
    invalid       = 5
    wont_fix      = 4
    in_progress   = 3
    fix_committed = 2
    fix_released  = 1
    # this will trigger an error with unique applied
    # by_design     = 4
    # closed        = 1

class tupleBugStatus(enum.Enum):
    """Enum members' values are not restricted to integers.
    in fact, any type of object can be associated with a member, using __init__()
    """
    new           = (7, ['incomplete', 'invalid', 'wont_fix', 'in_progress'])
    incomplete    = (6, ['new', 'wont_fix'])
    invalid       = (5, ['new'])
    wont_fix      = (4, ['new'])
    in_progress   = (3, ['new', 'fix_committed'])
    fix_committed = (2, ['in_progress', 'fix_released'])
    fix_released  = (1, ['new'])
    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions
    def can_transition(self, new_state):
        return new_state.name in self.transitions

class complexBugStatus(enum.Enum):
    """here is more complex enum
    """
    new = {
        'num': 7,
        'transitions': [
            'incomplete',
            'invalid',
            'wont_fix',
            'in_progress',
        ],
    }
    incomplete = {
        'num': 6,
        'transitions': ['new', 'wont_fix'],
    }
    invalid = {
        'num': 5,
        'transitions': ['new'],
    }
    wont_fix = {
        'num': 4,
        'transitions': ['new'],
    }
    in_progress = {
        'num': 3,
        'transitions': ['new', 'fix_committed'],
    }
    fix_committed = {
        'num': 2,
        'transitions': ['in_progress', 'fix_released'],
    }
    fix_released = {
        'num': 1,
        'transitions': ['new'],
    }
def __init__(self, vals):
    self.num = vals['num']
    self.transitions = vals['transitions']
def can_transition(self, new_state):
    return new_state.name in self.transitions

@addBreaker
def enum_create(e: enum):
    print('\nMember name : {}'.format(BugStatus.wont_fix.name))
    print('Member value: {}'.format(BugStatus.wont_fix.value))

@addBreaker
def enum_vs_dict():
    BugStatus = dict(
        new           = 7,
        incomplete    = 6,
        invalid       = 5,
        wont_fix      = 4,
        in_progress   = 3,
        fix_committed = 2,
        fix_released  = 1,
    )
    
    print('\nMember name : {}'.format(BugStatus.keys()))
    print('Member value: {}'.format(BugStatus['wont_fix'])) 

@addBreaker
def enum_iterate(e: enum):
    for status in e:
        print('{:15} = {}'.format(status.name, status.value))

@addBreaker
def enum_comp(e: enum):
    actual_state = e.wont_fix
    desire_state = e.fix_released

    print('Equality:', actual_state == desire_state, actual_state == e.wont_fix)
    print('Identity:', actual_state is desire_state, actual_state is e.wont_fix)

    print('Ordered by value:')
    try:
        print('\n'.join('  ' + s.name for s in sorted(e)))
    except TypeError as err:
        print('  cannot sort: {}'.format(err))

# TODOS: P107
@addBreaker
def enum_aliases(e: enum):
    for status in e:
        print('{:15} = {}'.format(status.name, status.value))
    print('\nSame: by_design is wont_fixs: ', e.by_design is e.wont_fix)
    print('Same: closed is fix_released: ', e.closed is e.fix_released)

@addBreaker
def enum_unique_enforce(e: enum):
    pass

@addBreaker
def enum_programmatic_create():
    # seems similar with collections.namedtuple()?
    BugStatus = enum.Enum(
        value = 'BugStatus',
        # control is limit using tuple
        names = ('fix_released fix_committed in_progress wont_fix invalid incomplete new'),
    )
    print('Member:  {}'.format(BugStatus))
    print('\nAll members:')
    for status in BugStatus:
        print('{:15} = {}'.format(status.name, status.value))

@addBreaker
def enum_programmatic_mapping():
    BugStatus = enum.Enum(
        value = 'BugStatus',
        # gain more control using list
        names = [
            ('new', 7),
            ('incomplete', 6),
            ('invalid', 5),
            ('wont_fix', 4),
            ('in_progress', 3),
            ('fix_committed', 2),
            ('fix_released', 1),
        ]
    )

    print('\nAll members:')
    for status in BugStatus:
        print('{:15} = {}'.format(status.name, status.value))

@addBreaker
def enum_tuple_values(e: enum):
    print('Name :', e.in_progress)
    print('Value:', e.in_progress.value)
    print()
    print('Custom attribute:', e.in_progress.transitions)
    print('Using attribute :', e.in_progress.can_transition(e.new))

@addBreaker
def enum_complex_values(e: enum):
    print('Name :', e.in_progress)
    print('Value:', e.in_progress.value)
    print()
    print('Custom attribute:', e.in_progress.transitions)
    print('Using attribute :', e.in_progress.can_transition(e.new))    



def main():
    # create enum
    enum_create(BugStatus)
    # i can't figure out what fuck merit from enum though. Dict() produces the same output with less lines of code, doesn't it?
    # tries to find out merit ..
    enum_vs_dict()
    # iterates an enum
    enum_iterate(BugStatus)
    # enum inner element comparison
    enum_comp(BugStatus)
    # enum.IntEnum
    enum_comp(intBugStatus)
    # in enum, different names have the same value
    enum_aliases(BugStatus)
    # require all members to have unique values using @Enum.unique
    enum_unique_enforce(uniBugStatus)
    # another way to create enumeration programmatically, rather than hard-coding in class definition..
    enum_programmatic_create()
    # gain more control using list when creating enumeration programmatically
    enum_programmatic_mapping()
    # tuple as value in enum
    enum_tuple_values(tupleBugStatus)

if __name__ == "__main__":
    main()