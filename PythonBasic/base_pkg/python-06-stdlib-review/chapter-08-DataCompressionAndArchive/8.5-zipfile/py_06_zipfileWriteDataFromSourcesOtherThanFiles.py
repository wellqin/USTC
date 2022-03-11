import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zipfile_writestr():
    msg = 'This data did not exist in a file.'
    with zipfile.ZipFile('writestr.zip',
                        mode='w',
                        compression=zipfile.ZIP_DEFLATED,
                        ) as zf:
        zf.writestr('from_string.txt', msg)
    with zipfile.ZipFile('writestr.zip', 'r') as zf:
        print(zf.read('from_string.txt'))

    pass


if __name__ == "__main__":
    # data in memory -> os sys buffer -> file on hd -> archive
    # shortcut: data in memory -> added to the zip archive, using `writestr()`
    zipfile_writestr()