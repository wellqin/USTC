import sys, shutil
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def shutil_which():
    # ! nice. it's a programmatic way to search path
    # unix-like os using which()
    # winos using where() <-- this does NOT work 
    print(shutil.which('EXCEL.EXE'))
    print(shutil.which('tox'))
    print(shutil.which('no-such-program'))

@addBreaker
def shutil_which_regular_file():
    import os
    path = 'C:/'
    mode = os.F_OK | os.R_OK
    filename = shutil.which(
        'EXCEL.EXE',
        mode=mode,
        path=path,
    )
    print(filename)

if __name__ == "__main__":
    shutil_which()
    # user defined which()
    shutil_which_regular_file()

