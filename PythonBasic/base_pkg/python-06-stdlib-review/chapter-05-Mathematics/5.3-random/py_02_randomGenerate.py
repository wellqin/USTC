import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_randomm():
    for _ in range(5):
        print('%04.3f' % random.random(), end=' ')
    return

@addBreaker
def random_uniform():
    for _ in range(5):
        print('%04.3f' % random.uniform(1, 100), end=' ')
    return

if __name__ == "__main__":
    # using random.random() if wanted float numbers 0<= n <1. normal distribution
    random_randomm()
    # using random.uniform() if wanted float numbers in x< n <y.
    # ! random.uniform() implementation formula `min + (max - min) * random.random()`
    random_uniform()