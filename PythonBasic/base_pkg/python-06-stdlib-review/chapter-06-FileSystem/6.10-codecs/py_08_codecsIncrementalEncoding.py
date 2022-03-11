import sys, codecs
sys.path.append('.')
from pkg.breaker import addBreaker
from codecs_to_hex import to_hex

@addBreaker
def codecs_incremental_bz2():
    text  = b'abcdefghijklmnopqrstuvwxyz\n'
    repet = 50
    print('Text length  :', len(text))
    print('Repetitions  :', repet)
    print('Expected len :', len(text) * repet)

    # encode the text several times to build up a large aumout of data
    encoder = codecs.getincrementalencoder('bz2')()
    encoded = []

    print()
    print('Encoding :', end=' ')
    last = repet - 1
    for i in range(repet):
        en_c = encoder.encode(text, final=(i == last))
        if en_c:
            print('\nEncoded : {} bytes'.format(len(en_c)))
            encoded.append(en_c)
        else:
            sys.stdout.write('.')
    all_encoded = b''.join(encoded)
    print()
    print('Total encoded length:', len(all_encoded))
    print()

    # decode
    decoder = codecs.getincrementaldecoder('bz2')()
    decoded = []
    print('Decoding:', end=' ')
    for i, b in enumerate(all_encoded):
        final = (i + 1) == len(text)
        c = decoder.decode(bytes([b]), final)
        if c:
            print('\nDecoded : {} characters'.format(len(c)))
            print('Decoding:', end=' ')
            decoded.append(c)
        else:
            sys.stdout.write('.')
    print()
    restored = b''.join(decoded)
    print()
    print('Total uncompressed length:', len(restored))
    pass

if __name__ == "__main__":
    codecs_incremental_bz2()