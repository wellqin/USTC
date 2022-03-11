import sys, gzip
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def gzip_BytesIO():
    from io import BytesIO
    import binascii
    uncompressed_data = b'The same line, over and over.\n' * 10
    print('UNCOMPRESSED:', len(uncompressed_data))
    print(uncompressed_data)
    buf = BytesIO()
    with gzip.GzipFile(mode='wb', fileobj=buf) as f:
        f.write(uncompressed_data)

    compressed_data = buf.getvalue()
    print('COMPRESSED:', len(compressed_data))
    print(binascii.hexlify(compressed_data))

    inbuffer = BytesIO(compressed_data)
    with gzip.GzipFile(mode='rb', fileobj=inbuffer) as f:
        reread_data = f.read(len(uncompressed_data))
    print('\nREREAD:', len(reread_data))
    print(reread_data)
    pass

if __name__ == "__main__":
    """
    The GzipFile class can be used to wrap other types of data streams
    so they can use compression as well. 
    This approach is useful when data is being transmitted over a socket or an existing (already open) file handle

    A BytesIO buffer can also be used with GzipFile for operations on data in memory
    """
    gzip_BytesIO()