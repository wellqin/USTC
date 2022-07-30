import itertools, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

def should_drop(x):
    print('Testing :', x)
    return x < 1

def should_take(x):
    print('Testing :', x)
    return x < 2

def check_item(x):
    print('Testing :', x)
    return x < 1

list_sample = [-1, 0, 1, 2, -2]

@addBreaker
def itertools_dropwhile():
    # ! see the behavior of dropwhile()?
    # A: dropwhile() doesn't filter every item of the input ..
    # after the condition is false the first time, all of the remaining items in the input are returned
    print('itertools.dropwhile(), cond: x < 1')
    for i in itertools.dropwhile(should_drop, list_sample):
        print('Yielding:', i)

@addBreaker
def itertools_takewhile():
    # ! yeah, takewhile() behaves as same as dropwhile()
    # takewhile() stops after the condition is false the first time too.
    print('itertools.takewhile(), cond: x < 2')
    for i in itertools.takewhile(should_take, list_sample):
        print('Yielding:', i)
    return

@addBreaker
def itertools_builtin_filter_vs_filterfalse():
    # builtin filter() behaves like this ..
    # ! filter() checks every item
    print('filter(), cond: x < 2')
    for i in filter(check_item, list_sample):
        print('Yielding:', i)

    # filterfalse(). be couple as always ..
    print('\nfilterfalse(), cond: x < 2')
    for i in itertools.filterfalse(check_item, list_sample):
        print('Yielding:', i)    
    return

@addBreaker
def itertools_compress():
    # ! instead of using a function, 
    # ! compress() uses the values in another iterable to indicate when to accept and when to ignore
    every_third = itertools.cycle([False, False, True])
    data        = range(1, 10)
    print('itertools.compress()')
    for i in itertools.compress(data, every_third):
        print('Yielding:', i)
    return

if __name__ == "__main__":
    # dropwhile
    itertools_dropwhile()
    # takewhile
    itertools_takewhile()
    # builtin filter vs itertools.filterfalse
    itertools_builtin_filter_vs_filterfalse()
    # itertools.compress
    itertools_compress()