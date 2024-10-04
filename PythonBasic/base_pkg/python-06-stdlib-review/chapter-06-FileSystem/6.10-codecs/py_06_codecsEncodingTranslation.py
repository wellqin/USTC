import sys, codecs, io
sys.path.append('.')
from pkg.breaker import addBreaker
from codecs_to_hex import to_hex

@addBreaker
def codecs_encodedfile():
    # raw version of the original data
    data   = 'français' 
    # manually encode it as utf8
    utf8   = data.encode('utf8')
    print('Start as UTF8    :', to_hex(utf8, 1))
    # set up an output buffer
    output = io.BytesIO()
    encoded_file = codecs.EncodedFile(
        output,
        data_encoding='utf8',
        file_encoding='utf16',
    )
    encoded_file.write(utf8)
    # fetch the buffer contents are a UTF16 encoded byte string
    utf16 = output.getvalue()
    print('Encoded to UTF16 :', to_hex(utf16, 2))

    # another buffer with UTF16 data for reading
    # and wrap it with another EncodedFile
    buffer = io.BytesIO(utf16)
    encoded_file = codecs.EncodedFile(
        buffer,
        data_encoding='utf8',
        file_encoding='utf16',
    )
    recoded = encoded_file.read()
    print('Back to UTF8     :', to_hex(recoded, 1))
    
    pass



if __name__ == "__main__":
    # the ability to change a file's encoding w/o holding on to that 
    # itermediate data format is sometimes useful.
    # ! EncodedFile() takes an open file handle using one encoding 
    # ! and wraps it with a class that translates the data to another encoding as the I/O occurs
    codecs_encodedfile()