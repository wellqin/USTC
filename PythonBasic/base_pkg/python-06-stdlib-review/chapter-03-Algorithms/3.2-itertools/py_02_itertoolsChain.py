import itertools, sys, os

from standard_library.package.algorithms import addBreaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


@addBreaker
def itertools_chain():
    a = [1, 2, 3]
    b = list('abc')
    # very small and smart ..
    for i in itertools.chain(a, b):
        print(i, end=' ')
    print()


@addBreaker
def itertools_zip_vs_zip_longest():
    a = [1, 2, 3]
    b = list('abc')
    c = list('abcd')
    # two same sizeof sequences ..
    print('zip two same sizeof sequences: {!r}, {!r}'.format(a, b))
    for i, j in zip(a, b):
        print(i, j)
    print('ziplongest two same sizeof sequences: {!r}, {!r}'.format(a, b))
    for i, j in itertools.zip_longest(a, b):
        print(i, j)
    # two NOT same sizeof sequences ..
    print('zip two NOT same sizeof sequences: {!r}, {!r}'.format(a, c))
    for i, j in zip(a, c):
        print(i, j)
    print('ziplongest two NOT same sizeof sequences: {!r}, {!r}'.format(a, c))
    # using optionoal *fillvalue* argument to substitute default None for any missing values 
    for i, j in itertools.zip_longest(a, c, fillvalue='lol'):
        print(i, j)


@addBreaker
def itertools_islice():
    print('Stop at index 5:')
    for i in itertools.islice(range(100), 5):
        print(i, end=' ')
    print('\n')
    print('Start at index 5, Stop at index 10:')
    for i in itertools.islice(range(100), 5, 10):
        print(i, end=' ')
    print('\n')
    print('By tens to 100:')
    for i in itertools.islice(range(100), 0, 100, 10):
        print(i, end=' ')
    print('\n')


@addBreaker
def itertools_tee():
    r = itertools.islice(itertools.count(), 5)
    i1, i2 = itertools.tee(r)
    # ? do u know what happens if list(r) here?
    # A: r is exhausted :^)
    # print('\nlist(r):', list(r))

    print('r :', end=' ')
    for i in r:
        print(i, end=' ')
        if i > 1:
            break
    print('i1:', list(i1))
    print('i2:', list(i2))


if __name__ == "__main__":
    # chaining small sequences w/o actual forming a big list..
    itertools_chain()
    # zip vs zip_the_longest
    itertools_zip_vs_zip_longest()
    # uses itertools.islice() to slice sequences
    itertools_islice()
    # tee (tried to search what does 'tee' stand for. no chance. 
    # my guess is 'teardown')
    # NOPE. tee is originated from Linux/Unix system tee command(T-splitter), 
    # see graph on webpage -- https://www.geeksforgeeks.org/tee-command-linux-example/
    itertools_tee()
