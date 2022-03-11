import pathlib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def pathlib_operator():
    usr = pathlib.PureWindowsPath('/usr')
    print(usr)

    usr_local = usr / 'local'
    print(usr_local)

    usr_share = usr / pathlib.PureWindowsPath('share')
    print(usr_share)

    root = usr / '..'
    print(root)

    etc = root / '/etc'
    print(etc)
    
    return

@addBreaker
def pathlib_resolve():
    usr_local = pathlib.Path('/usr/local')
    share     = usr_local / '..' / 'share'
    print(share.resolve())

@addBreaker
def pathlib_joinpath():
    root      = pathlib.PureWindowsPath('/')
    subdirs   = ['usr', 'local']
    usr_local = root.joinpath(*subdirs)
    print(usr_local)

@addBreaker
def pathlib_from_existing():
    ind = pathlib.PureWindowsPath(__file__)
    print(ind)
    # with_name() creates a new path that replace the name portion of a path with a different filename
    py = ind.with_name('pathlib_from_existing.py')
    print(py)
    # with_suffix() creates a new path that replace the filename's extension with a different value
    pyc = py.with_suffix('.pyc')
    print(pyc)

if __name__ == "__main__":
    # ! builds paths
    pathlib_operator()
    # ! Path.resolve() normalizes a path by looking at the file system
    # for directories and symbolic links
    # and produces the absolute path referred to by a name
    pathlib_resolve()
    # ! joinpath() builds paths when the segments are not known in advance
    pathlib_joinpath()
    # ! with_name() vs with_suffix(). both methods return new obj, and the original is left unchanged
    pathlib_from_existing()
    