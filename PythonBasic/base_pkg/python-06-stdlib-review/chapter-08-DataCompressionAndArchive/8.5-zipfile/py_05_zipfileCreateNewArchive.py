import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zipfile_write():
    with zipfile.ZipFile('write.zip', 'w') as zf:
        print('adding README.txt')
        zf.write('README.txt')
    pass

@addBreaker
def zipfile_write_compression():
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED
    modes = {
        zipfile.ZIP_DEFLATED: 'deflated',
        zipfile.ZIP_STORED: 'stored',
    }
    print('creating archive')   
    with zipfile.ZipFile('write_compression.zip', mode='w') as zf:
        mode_name = modes[compression]
        print('adding README.txt with compression mode', mode_name)
        zf.write('README.txt', compress_type=compression)
    print()

@addBreaker
def zipfile_write_arcname():
    with zipfile.ZipFile('write_arcname.zip', mode='w') as zf:
        zf.write('README.txt', arcname='NOT_README.txt')

    pass


if __name__ == "__main__":
    # by default, zipfile.ZipFile() is `STORE`.
    # using zlib to compress each file
    zipfile_write()
    # alternative name
    zipfile_write_arcname