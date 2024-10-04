import sys, io
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def io_TextIOWrapper():
    output  = io.BytesIO()
    wrapper = io.TextIOWrapper(
        output,
        encoding='utf8',
        write_through=True,
    )
    wrapper.write('This goes into the buffer.')
    wrapper.write('ÁÇÊ')
    print(output.getvalue())
    print(output.getbuffer())
    output.close()

    input = io.BytesIO(
        b'Inital value for read buffer with unicode characters ' + 'ÁÇÊ'.encode('utf8')
    )
    wrapper = io.TextIOWrapper(input, encoding='utf8')
    print(wrapper.read())



if __name__ == "__main__":
    io_TextIOWrapper()