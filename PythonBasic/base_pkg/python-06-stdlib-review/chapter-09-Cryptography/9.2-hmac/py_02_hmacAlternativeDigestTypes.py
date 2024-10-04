import sys, hmac
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def hmac_sha():
    digest_maker = hmac.new(
        b'secret-key-goes-here',
        b'',
        'sha1',
    )

    with open(__file__, 'rb') as f:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    digest = digest_maker.hexdigest()
    print(digest)
    pass

if __name__ == "__main__":
    # new() function takes 3 arguments.
    # first   -- is the secret key, which should be shared between the two endpoints that are communicating so both ends can use the same value
    # sencond -- is an intial messsage
    # third   -- is the digest module to be used. the default is `hashlib.md5`, but this example passes `sha1`, causing `hmac` to use `hashlib.sha1` instead
    hmac_sha()