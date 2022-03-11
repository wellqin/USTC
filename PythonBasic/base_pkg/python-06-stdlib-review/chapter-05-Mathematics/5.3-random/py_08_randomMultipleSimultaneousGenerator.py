import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_random_class():
    import time
    # ? why?
    # differenct instances have different internal states. which is `standalone`, good for some situation
    # but it's possible to synchronize them to obtain same values by using same `seed`
    print('default initialization:\n')
    r1 = random.Random()
    r2 = random.Random()
    for _ in range(3):
        print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))
    print('\nsame seed:\n')
    seed = time.time()
    r1 = random.Random(seed)
    r2 = random.Random(seed)
    for _ in range(3):
        print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))

    return

if __name__ == "__main__":
    # 
    random_random_class()
    # Random class
    random_random_class()