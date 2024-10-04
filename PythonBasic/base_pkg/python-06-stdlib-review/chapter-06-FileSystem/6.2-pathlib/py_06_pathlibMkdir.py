import pathlib, sys
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def pathlib_mkdir():
    p = pathlib.Path('example_dir')
    print('Creating {}'.format(p))
    try:
        p.mkdir() 
    except FileExistsError:
        pass
    return

@addBreaker
def pathlib_symlink_to():
    p = pathlib.Path('example_link')
    # ! need UAC authority
    p.symlink_to('readme.md')
    print(p)
    print(p.resolve().name)
    return

if __name__ == "__main__":
    # p.mkdir()
    pathlib_mkdir()
    # p.symlink_to
    # pathlib_symlink_to()