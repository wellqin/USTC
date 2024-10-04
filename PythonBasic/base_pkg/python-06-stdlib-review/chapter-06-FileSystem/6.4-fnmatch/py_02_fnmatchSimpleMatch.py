import sys, fnmatch
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def fnmatch_fnmatch():
    import os
    pattern = 'fnmatch_*.py'
    print('Pattern  :', pattern)
    print()
    # ! ZANNEN, pathlib does NOT have listdir() functionality ..
    files = os.listdir('.')
    for name in files:
        print('Filename: {:<25} {}'.format(
            name, fnmatch.fnmatch(name, pattern)
        ))
    pass

@addBreaker
def fnmatch_fnmatchcase():
    import os
    pattern = 'FNMATCH_*.PY'
    print('Pattern :', pattern)
    print()

    files = os.listdir('.')
    for name in files:
        print('Filename: {:<25} {}'.format(
            name, fnmatch.fnmatchcase(name, pattern)
        ))

if __name__ == "__main__":
    # simple match
    fnmatch_fnmatch()
    # case sensitive
    fnmatch_fnmatchcase()