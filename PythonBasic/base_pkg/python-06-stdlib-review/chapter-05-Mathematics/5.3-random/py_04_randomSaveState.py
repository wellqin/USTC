import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_state():
    import pathlib, pickle
    p = pathlib.Path('state.dat')
    if p.exists():
        print('Found state.dat, initializing random module')
        with open(p, 'rb') as f:
            state = pickle.load(f)
        # ? pairs: random.setstate() vs random.getstate(). bingo!
        random.setstate(state)
    else:
        # use a well-know stat state
        print('No state.dat. seeding')
        random.seed(1)
    # produce random values
    for _ in range(3):
        print('{:04.3f}'.format(random.random()), end=' ')
    print()
    # save state for next time
    with open(p, 'wb') as f:
        pickle.dump(random.getstate(), f)
    # produce more random values
    print('\nafter saving state:')
    for _ in range(3):
        print('{:04.3f}'.format(random.random()), end=' ')
    print()

if __name__ == "__main__":
    random_state()