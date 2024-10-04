import sys, hashlib
sys.path.append('.')
from pkg.breaker import addBreaker
from hashlib_data import lorem

@addBreaker
def hashlib_sha1():
    h = hashlib.sha1()
    h.update(lorem.encode('utf8'))
    print(h.hexdigest())
    
    pass


if __name__ == "__main__":
    hashlib_sha1()