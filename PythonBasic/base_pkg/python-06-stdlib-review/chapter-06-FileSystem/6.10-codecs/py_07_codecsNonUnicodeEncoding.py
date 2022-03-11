import sys, codecs
sys.path.append('.')
from pkg.breaker import addBreaker
import io
from codecs_to_hex import to_hex

@addBreaker
def codecs_rot13():
    buffer = io.StringIO()
    stream = codecs.getwriter('rot_13')(buffer) 
    text   = 'abcdefghijklmnopqrstuvwxyz'
    stream.write(text)
    stream.flush()
    print('Original :', text)
    print('ROT-13   :', buffer.getvalue())

@addBreaker
def codecs_zlib():
    buffer = io.BytesIO()
    stream = codecs.getwriter('zlib')(buffer)
    text   = b'abcdefghijklmnopqrstuvwxyz\n' * 50
    stream.write(text)
    stream.flush()
    print('Original length  :', len(text))
    compressed_data = buffer.getvalue()
    print('ZIP compressed   :', len(compressed_data))
    buffer = io.BytesIO(compressed_data)
    stream = codecs.getreader('zlib')(buffer)
    first_line = stream.readline()
    print('Read first line  :', repr(first_line))
    uncompressed_data = first_line + stream.read()
    print('Uncompressed     :', len(uncompressed_data))
    print('Same             :', text==uncompressed_data)
    pass



if __name__ == "__main__":
    # another encoding
    codecs_rot13()
    # another encoding
    codecs_zlib()