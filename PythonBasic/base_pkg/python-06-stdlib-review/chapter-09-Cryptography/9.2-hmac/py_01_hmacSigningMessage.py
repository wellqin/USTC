import sys, hmac
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def hmac_simple():
    digest_maker = hmac.new(b'secret-shared-key-goes-here')
    lorem = r'chapter-09-Cryptography\9.2-hmac\lorem.txt'
    with open(lorem, 'rb') as f:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    digest = digest_maker.hexdigest()
    print(digest)
    pass

if __name__ == "__main__":
    hmac_simple()