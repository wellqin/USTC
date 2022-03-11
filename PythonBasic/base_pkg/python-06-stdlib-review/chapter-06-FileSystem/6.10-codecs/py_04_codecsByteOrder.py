"""
`endianness`

`BOM`(bytes-order marker)
"""

import sys, codecs
sys.path.append('.')
from pkg.breaker import addBreaker
from codecs_to_hex import to_hex

# ? wtf are these BOM abbreviated for?
BOM_TYPES = [
    'BOM', 'BOM_BE', 'BOM_LE',
    'BOM_UTF8',
    'BOM_UTF16', 'BOM_UTF16_BE', 'BOM_UTF16_LE', 
    'BOM_UTF32', 'BOM_UTF32_BE', 'BOM_UTF32_LE',
]

@addBreaker
def codecs_bom():
    for name in BOM_TYPES:
        print('{:12} : {}'.format(
            name, to_hex(getattr(codecs, name), 2)
        ))

@addBreaker
def codecs_bom_create_file():
    if codecs.BOM_UTF16 == codecs.BOM_UTF16_BE:
        bom      = codecs.BOM_UTF16_LE
        encoding = 'utf_16_le'
    else:
        bom      = codecs.BOM_UTF16_BE
        encoding = 'utf_16_be'
    print('Native order     :', to_hex(codecs.BOM_UTF16, 2))
    print('Selected order   :', to_hex(bom, 2))

    # encode the text
    encoded_text = 'français'.encode(encoding)
    print('{:14}   : {}'.format(encoding, to_hex(encoded_text, 2)))

    # write
    with open('nonnative-encoded.txt', 'wb') as f:
        f.write(bom)
        f.write(encoded_text)

@addBreaker
def codecs_bom_detection():
    # look at the raw data
    with open('nonnative-encoded.txt', mode='rb') as f:
        raw_bytes = f.read()
    print('Raw      :', to_hex(raw_bytes, 2))
    # reopen the file and let codecs detect the BOM
    # ! BUT encoding is known beforehand. isn't this cheating?
    with codecs.open('nonnative-encoded.txt', mode='r', encoding='utf-16') as f:
        decoded_text = f.read()
    print('Decoded  :', repr(decoded_text))


if __name__ == "__main__":
    # endianness -> BOM types
    codecs_bom()
    # create a file using BOM
    codecs_bom_create_file()
    # read data from the file and decode
    codecs_bom_detection()