import sys, hashlib
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def hashlib_algorithms():
    print("guaranteed: ", sorted(hashlib.algorithms_guaranteed))
    print("available : ", sorted(hashlib.algorithms_available))
    pass

if __name__ == "__main__":
    # some algorithms are available on all platform, `algorithms_guaranteed`
    # some depend on the underlying libraries.       `algorithms_available`
    hashlib_algorithms()