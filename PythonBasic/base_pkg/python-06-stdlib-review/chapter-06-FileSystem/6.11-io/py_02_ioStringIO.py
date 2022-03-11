import sys, io
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def io_StringIO():
    # write to a buffer
    output = io.StringIO()
    output.write('This goes into the buffer ..')
    print('And so does this.', file=output)
    print(output.getvalue())    # retrieve the value written
    output.close()  # discard buffer memory
    input = io.StringIO('Initial value for read buffer') # initializes a read buffer
    print(input.read()) # read from the buffer
    pass

@addBreaker
def io_BytesIO():
    # write into a memory buffer
    output = io.BytesIO()
    output.write('This goes into the buffer.'.encode('utf8'))
    output.write('ÁÇÊ'.encode('utf8'))
    print(output.getvalue())
    output.close()

    input = io.BytesIO(b'Initial value for read buffer')
    print(input.read())    
    pass


if __name__ == "__main__":
    # string stream can be read(), write(), readline(), and readlines()
    # also seek()
    io_StringIO()
    # BytesIO
    io_BytesIO()