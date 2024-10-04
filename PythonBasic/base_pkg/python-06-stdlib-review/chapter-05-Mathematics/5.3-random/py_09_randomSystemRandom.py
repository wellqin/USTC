import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_system_random():
    # ? why
    # some systems provide a random number generator that has access to more source of entropy
    # that can be introduced into the generator
    # random expose this feature throu `SystemRandom` class
    # ! sequences produced by `SystemRandom` class are not reproducible
    # ! because the randomness is coming from the system, rather than the software state.
    # * so `seed` and `setstate()` have no effect at all 
    import time
    print('default initialization:\n')
    r1 = random.SystemRandom()
    r2 = random.SystemRandom()
    for _ in range(3):
        print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))
    print('\nsame seed:\n')
    seed = time.time()
    r1 = random.SystemRandom(seed)
    r2 = random.SystemRandom(seed)
    for _ in range(3):
        print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))
    print('\nsame seed:\n')
    
    return

if __name__ == "__main__":
    random_system_random()