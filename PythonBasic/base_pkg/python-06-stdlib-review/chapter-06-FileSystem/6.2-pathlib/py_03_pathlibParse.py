import pathlib, sys, os
# ahh, sys.path.append(p: str)..
# i'm glab to ditch os.path.dirname() nesting approach
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))
from pkg.breaker import addBreaker

@addBreaker
def pathlib_parts():
    p = pathlib.Path(__file__)
    print(p.parts)

    p1 = pathlib.Path(__file__).parent.parent.parent
    p2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # ! pathlib returns pathlib.WindowsPath obj
    # * uses str(pathlib.Path obj) to convert
    print('pathlib: {}, type: {}'.format(p1, type(p1)))
    # ! pathlib returns str obj
    print('os.path: {}, type: {}'.format(p2, type(p2)))
    assert str(p1) == p2    # assertionError. why? path separators differs
    return

@addBreaker
def pathlib_name():
    p = pathlib.Path(__file__)
    # ! this is an elegant way, vs os.path.splitext()
    print('path     :   {}'.format(p))
    print('name     :   {}'.format(p.name))
    print('suffix   :   {}'.format(p.suffix))
    print('stem     :   {}'.format(p.stem))

if __name__ == "__main__":
    # parts property produces a sequence of path segments parsed based on the path separator value
    pathlib_parts()
    # path properties
    pathlib_name()