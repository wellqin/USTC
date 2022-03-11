"""

Table: codecs Error Handling Modes
P411/1454

+--------------------+------------------------------------------------------------------------+
|   Error Mode       | Desc                                                    
+====================+========================================================================+
|   strict           | Raises an exception if the data cannot be converted     
+--------------------+------------------------------------------------------------------------+
|   replace          | Substitutes a special marker character for data that cannot be encoded
+--------------------+------------------------------------------------------------------------+
|   ignore           | Skips the data
+--------------------+------------------------------------------------------------------------+
|  xmlcharrefreplace | XML character (encoding only)
+--------------------+------------------------------------------------------------------------+
|  backslashreplace  | Escape sequence (encoding only)                                        |
+--------------------+------------------------------------------------------------------------+



"""


import sys, codecs
sys.path.append('.')
from pkg.breaker import addBreaker
import random
from codecs_to_hex import to_hex

@addBreaker
def codecs_encode_error():
    error_handling = random.choice('strict replace ignore xmlcharrefreplace backslashreplace'.split(' ')) 
    print('error_handling:', error_handling)
    text           = 'français'
    try:
        with codecs.open('encode_error.txt', 'w', encoding='ascii', errors=error_handling) as f:
            f.write(text)
    except UnicodeEncodeError as err:
        print('ERROR:', err)
    else:
        with open('encode_error.txt', 'rb') as f:
            print('File contents: {!r}'.format(f.read()))
    
@addBreaker
def codecs_decode_error():
    error_handling = random.choice('strict replace ignore'.split(' ')) 
    print('error_handling:', error_handling)
    text           = 'français'
    print('Original      :', repr(text))

    with codecs.open('decode_error.txt', 'w', encoding='utf16') as f:
        f.write(text)
    with open('decode_error.txt', 'rb') as f:
        print('File contents :', to_hex(f.read(), 1))
    with codecs.open(
        'decode_error.txt',
        'r',
        encoding='utf8',
        errors=error_handling,
    ) as f:
        try:
            data = f.read()
        except UnicodeDecodeError as err:
            print('ERROR         :', err)
        else:
            print('Read          :', repr(data))


if __name__ == "__main__":
    # encoding error by passing errors argument
    codecs_encode_error()
    # decoding error by passing errors argument
    codecs_decode_error()