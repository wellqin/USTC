import sys, unicodedata
sys.path.append('.')
from pkg.breaker import addBreaker
from codecs_to_hex import to_hex

@addBreaker
def codecs_encodings():
    text = 'français'
    print('Raw      : {!r}:'.format(text))
    for c in text:
        print('      {!r}: {}'.format(c, unicodedata.name(c, c)))
    print('UTF-8    : {!r}'.format(to_hex(text.encode('utf8'), 1)))
    print('UTF-16   : {!r}'.format(to_hex(text.encode('utf16'), 2)))

@addBreaker
def codecs_decode():
    text    = 'français'
    encoded = text.encode('utf8')
    decoded = encoded.decode('utf8')
    print('Original :', repr(text))
    print('Encoded  :', to_hex(encoded, 1), type(encoded))
    print('Decoded  :', repr(decoded), type(decoded))

if __name__ == "__main__":
    # ? one second, wth no `codecs`module used?
    # ! encoding
    codecs_encodings()
    # ! decoding
    codecs_decode()