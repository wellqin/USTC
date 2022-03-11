import sys, pathlib, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# ? or
# sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))
# ? or
# sys.path.append(str(pathlib.Path.cwd()))
# ? or
# sys.path.append(os.curdir)
# ? or
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def pathlib_convenience():
    home = pathlib.Path.home()
    cwd  = pathlib.Path.cwd()
    print('home :', home)
    print('cwd  :', cwd)
    return

@addBreaker
def pathlib_iterdir():
    p = pathlib.Path('.')
    for f in p.iterdir():
        print(f)
    return

@addBreaker
def pathlib_glob_vs_rglob():
    p = pathlib.Path('.')
    print('pathlib.Path.glob("*.py"):')
    for f in p.glob('*.py'):
        print(f)
    # ! glob() recursive scanning using the pattern prefix ** 
    # ! or rglob()
    # * this is way better than os.walk() plus glob.glob() ...
    print('\npathlib.Path.glob("./**/*.py")')
    for f in p.glob('./**/*.py'):
        print(f)
    print('\npathlib.Path.rglob("*.py"):')
    for f in p.rglob('*.py'):
        print(f)
    return

if __name__ == "__main__":
    # creates concrete paths
    pathlib_convenience()
    # Path.iterdir()
    pathlib_iterdir()
    # glob()
    pathlib_glob_vs_rglob()