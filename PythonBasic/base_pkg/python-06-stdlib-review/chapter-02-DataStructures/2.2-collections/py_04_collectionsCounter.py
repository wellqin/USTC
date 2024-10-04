import collections, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def collecitons_counter_init():
    print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
    print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
    print(collections.Counter(a=2, b=3, c=1))

@addBreaker
def collections_counter_update():
    c = collections.Counter()
    print('Initial :', c)
    # ! the behavior of Counter.update() differs from normal dict(). "increment" rather than "replace"
    c.update('abcdaab')
    print('Sequence:', c)
    c.update({'a': 1, 'd': 5})
    print('Dict    :', c)

@addBreaker
def collections_counter_get_values():
    c = collections.Counter('abcdaab')
    # ! Counter wont throw KeyError even the key doesnt exist. it returns 0
    for letter in 'abcde':
        print('{} : {}'.format(letter, c[letter]))

@addBreaker
def collections_counter_elements():
    c = collections.Counter('extremely')
    c['z'] = 0
    print(c)
    # Counter().elements() 
    print(list(c.elements()))
    print('Counter().elements(): ', c.elements())

@addBreaker
def collections_counter_most_common():
    dummy_text = """
    Ipsum nostrud nostrud consectetur est enim nostrud amet ut eu aute ex. Laborum dolore exercitation elit aliquip. Dolore qui id magna ipsum. Commodo culpa labore ullamco elit duis magna proident eiusmod do. Minim esse est occaecat excepteur exercitation sint.
    Mollit laborum incididunt eu ad laboris proident aliquip laboris. Cupidatat id anim duis culpa elit ipsum ea ullamco velit laborum. Aute excepteur irure eu voluptate fugiat excepteur labore irure amet deserunt aliqua minim. Sunt aute proident id commodo aute tempor esse culpa enim. Mollit ea laboris commodo voluptate reprehenderit est commodo sit. Adipisicing non Lorem anim magna. Eu fugiat labore dolore laborum dolore.
    """
    file_path = os.path.join(os.path.dirname(__file__), 'words')
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w') as f:
        f.write(dummy_text)
    c = collections.Counter()
    with open(file_path, 'rt') as f:
        for line in f:
            c.update(line.rstrip().lower())
    print('Most common:')
    for letter, count in c.most_common(3):
        print('{!r}: {:>7}'.format(letter, count))

@addBreaker
def collections_counter_arithmetic():
    c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
    c2 = collections.Counter('alphabet')
    # interesting behaviors. aha, just like set objects. 
    # ! items with negative or zero values will be discard. again, "increment/decrement" rather than "replace"
    print('C1:', c1)
    print('C2:', c2)
    print('\nCombined counts:')
    print(c1 + c2)
    print('\nSubtraction:')
    print(c1 - c2)
    print('\nIntersection (taking positive minimums):')
    print(c1 & c2)
    print('\nUnion (taking maximums):')
    print(c1 | c2)

def main():
    # normal usage
    collecitons_counter_init()
    # update a Counter
    collections_counter_update()
    # access elements in Counter, behaves like dict()
    collections_counter_get_values()
    # using Counter().elements()
    collections_counter_elements()
    # most_common(n)
    collections_counter_most_common()
    # two counter arithmetic
    collections_counter_arithmetic()

if __name__ == "__main__":
    main()