import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker


@addBreaker
def zipfile_pyzipfile():
    with zipfile.PyZipFile('pyzipfile.zip', mode='w') as zf:
        zf.debug = 3
        print('Adding python files')
        zf.writepy('.')
    for name in zf.namelist():
        print(name)
    print()
    sys.path.insert(0, 'pyzipfile.zip')
    import zipfile_pyzipfile
    print('Imported from:', zipfile_pyzipfile.__file__)
    pass


if __name__ == "__main__":
    # 69 nice. `zipimport` modules from inside ZIP archive.
    # wait a second, what is the merit?
    # these archives must appear in `sys.path` 
    zipfile_pyzipfile()