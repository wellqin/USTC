import sys, hmac
sys.path.append('.')
from pkg.breaker import addBreaker
import hashlib, io, pickle

def make_digest(message: str) -> str:
    h = hmac.new(
        b'secret-shared-key-goes-here',
        message,
        hashlib.sha1,
    )
    return h.hexdigest().encode('utf8')

class SimpleObject:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name


@addBreaker
def hmac_pickle():
    # simulates a writable socket or pipe with a buffer
    out_s = io.BytesIO()
    # writes a valid object to the stream
    o = SimpleObject('digest matches')
    pickled_data = pickle.dumps(o)
    digest = make_digest(pickled_data)
    header = b'%s %d\n' % (digest, len(pickled_data))
    print('WRITING: {}'.format(header))
    out_s.write(header)
    out_s.write(pickled_data)

    # Write an invalid object to the stream.
    o = SimpleObject('digest does not match')
    pickled_data = pickle.dumps(o)
    digest = make_digest(b'not the pickled data at all')
    header = b'%s %d\n' % (digest, len(pickled_data))
    print('\nWRITING: {}'.format(header))
    out_s.write(header)
    out_s.write(pickled_data)
    out_s.flush()

    # Simulate a readable socket or pipe with a buffer.
    in_s = io.BytesIO(out_s.getvalue())
    # Read the data.
    while True:
        first_line = in_s.readline()
        if not first_line:
            break
        incoming_digest, incoming_length = first_line.split(b' ')
        incoming_length = int(incoming_length.decode('utf-8'))
        print('\nREAD:', incoming_digest, incoming_length)
    
        incoming_pickled_data = in_s.read(incoming_length)
        actual_digest = make_digest(incoming_pickled_data)
        print('ACTUAL:', actual_digest)
        if hmac.compare_digest(actual_digest, incoming_digest):
            obj = pickle.loads(incoming_pickled_data)
            print('OK:', obj)
        else:
            print('WARNING: Data corruption')
        pass

if __name__ == "__main__":
    # HMAC authentication should be used for any public network service
    # and anytime data is stored where security is important
    hmac_pickle()