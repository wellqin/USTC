import sys, hmac
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def hmac_base64():
    import hashlib, base64
    lorem = r'chapter-09-Cryptography\9.2-hmac\lorem.txt'
    with open(lorem, 'rb') as f:
        body = f.read()
    h = hmac.new(
        b'secret-shared-key-goes-here',
        body,
        hashlib.sha1,
    )
    digest = h.digest()
    print(base64.encodebytes(digest))
    pass

if __name__ == "__main__":
    # google checkout, amazon s3 use the base64 encoded version of the binary digest instead of the hexdigest
    # hex: 16bit
    # ohh, `base64` is also an encoding/decoding module
    hmac_base64()