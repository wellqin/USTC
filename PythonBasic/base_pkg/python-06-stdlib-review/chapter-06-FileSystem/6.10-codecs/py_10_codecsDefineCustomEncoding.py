import sys
sys.path.append('.')
from pkg.breaker import addBreaker
import string, codecs

@addBreaker
def invertcaps(text):
    return ''.join(
        c.upper() if c in string.ascii_lowercase
        else c.lower() if c in string.ascii_uppercase
        else c
        for c in text
    )

@addBreaker
def codecs_invertcaps_charmap():
    decoding_map = codecs.make_identity_dict(range(256))
    pairs = list(zip(
        [ord(c) for c in string.ascii_lowercase],
        [ord(c) for c in string.ascii_uppercase],
    ))
    decoding_map.update({
        upper: lower
        for (lower, upper)
        in pairs
    })
    decoding_map.update({
        lower: upper
        for (lower, upper)
        in pairs
    })
    encoding_map = codecs.make_identity_dict(decoding_map)
    # test
    print(codecs.charmap_encode('abcDEF', 'strict', encoding_map))
    print(codecs.charmap_decode(b'abcDEF', 'strict', decoding_map))
    print(encoding_map == decoding_map)

    text = 'pi: \u03c0'
    for error in ['ignore', 'replace', 'strict']:
        try:
            encoded = codecs.charmap_encode(text, error, encoding_map)
        except UnicodeEncodeError as err:
            encoded = str(err)
        print('{:7} : {}'.format(error, encoded))

@addBreaker
def codecs_register():
    def search1(encoding):
        print('search1: Searching for:', encoding)
        return None
    def search2(encoding):
        print('search2: Searching for:', encoding)
        return None

    codecs.register(search1)
    codecs.register(search2)

    utf8  = codecs.lookup('utf8')
    print('UTF8  :', utf8)
    try:
        unknow = codecs.lookup('no-such-encoding')
        print(unknow)
    except LookupError as err:
        print('ERROR  :', err)

@addBreaker
def codecs_invertcaps_register():
    # P425 / 1454
    pass



if __name__ == "__main__":
    # this implementation is NOT efficient, 
    # especially for large text strings
    print(invertcaps('ABCdef'))
    print(invertcaps('abcDEF'))
    # user defined codecs encoding
    codecs_invertcaps_charmap()
    # code
    codecs_register()