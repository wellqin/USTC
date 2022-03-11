import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_seed():
    random.seed(1)
    for _ in range(5):
        print('{:04.3f}'.format(random.random()), end=' ')
    print()
    return

if __name__ == "__main__":
    random_seed()