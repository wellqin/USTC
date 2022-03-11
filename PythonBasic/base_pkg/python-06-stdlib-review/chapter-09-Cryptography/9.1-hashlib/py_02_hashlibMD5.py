import sys, hashlib
sys.path.append('.')
from pkg.breaker import addBreaker
from hashlib_data import lorem

@addBreaker
def hashlib_md5_example():
    h = hashlib.md5() # construct a hash object
    h.update(lorem.encode('utf8')) # add data
    print(h.hexdigest()) # digest() or hexdigest()
    pass

if __name__ == "__main__":
    hashlib_md5_example()