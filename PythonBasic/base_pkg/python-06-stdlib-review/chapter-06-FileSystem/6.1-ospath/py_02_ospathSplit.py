import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def ospath_components():
    """platform based"""
    l = [
        os.sep,
        os.extsep,
        os.pardir,
        os.curdir,
    ]
    for i in l:
        print(i)

@addBreaker
def ospath_split():
    PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
    ]
    print('os.path.split():')
    for path in PATHS:
        print('{!r:17} : {}'.format(path, os.path.split(path)))
    # get first part of os.path.split()
    print('\nos.path.dirname():')
    for path in PATHS:
        print('{!r:17} : {!r}'.format(path, os.path.dirname(path)))
    print('\nos.path.basename():')
    # get second part of os.path.split()
    for path in PATHS:
        print('{!r:17} : {!r}'.format(path, os.path.basename(path)))

@addBreaker
def ospath_splitext():
    PATHS = [
        'filename.txt',
        'filename',
        '/path/to/filename.txt',
        '/',
        '',
        'my-archive.tar.gz',
        'no-extension.',
    ]
    print('\nos.path.splitext():')
    for path in PATHS:
        print('{!r:>21} : {!r}'.format(path, os.path.splitext(path)))

@addBreaker
def ospath_commonprefix_vs_commonpath():
    paths = [
        '/one/two/three/four',
        '/one/two/threefold',
        '/one/two/three/',        
    ]
    # ! commonprefix() -- path separator is NOT included in the consideration
    for path in paths:
        print('PATH:', path)
    print()
    print('commonprefix PREFIX:', os.path.commonprefix(paths))
    # ! commonpath() -- does honor path separators
    print('commonpath PREFIX  :', os.path.commonpath(paths))

@addBreaker
def ospath_expanduser_vs_expandvars():
    for user in ['', 'dhellmann', 'nosuchuser']:
        lookup = '~' + user
        print('{!r:15} : {!r}'.format(lookup, os.path.expanduser(lookup)))

@addBreaker
def ospath_normpath_vs_abspath():
    PATHS = [
        'one//two//three',
        'one/./two/./three',
        'one/../alt/two/three',
    ]
    
    print('os.path.normpath():')
    # ! clear embeded variables or extra separators
    for path in PATHS:
        print('{!r:>22} : {!r}'.format(path, os.path.normpath(path)))
    print('\nos.path.abspath():')
    # ! converts relative path to an absolute filename
    for path in PATHS:
        print('{!r:>22} : {!r}'.format(path, os.path.abspath(path)))
    return

@addBreaker
def ospath_properties():
    import time
    print('File         :', __file__)
    print('Access time  :', time.ctime(os.path.getatime(__file__)))
    print('Modified time:', time.ctime(os.path.getmtime(__file__)))
    print('Change time  :', time.ctime(os.path.getctime(__file__)))
    print('Size         :', os.path.getsize(__file__))
    return

@addBreaker
def ospath_tests():
    FILENAMES = [
        os.path.dirname(__file__),
        '/',
        './broken_link',
    ]
    for file in FILENAMES:
        print('File             : {!r}'.format(file))
        print('Absolute         :', os.path.isabs(file))
        print('Is File?         :', os.path.isfile(file))
        print('Is Dir?          :', os.path.isdir(file))
        print('Is Link?         :', os.path.islink(file))
        # ! ismount shorts for hard-driver
        print('Mountpoint?      :', os.path.ismount(file))
        print('Exists?          :', os.path.exists(file))
        # ! lexists shorts for link-exists
        print('Link Exists?     :', os.path.lexists(file))
        print()
    return


if __name__ == "__main__":
    # ospath components
    ospath_components()
    # ospath split
    ospath_split()
    # os.path.splitext()
    ospath_splitext()
    # commonprefix()
    ospath_commonprefix_vs_commonpath()
    # expanduser() vs expandvars()
    ospath_expanduser_vs_expandvars()
    # normpath() vs abspath()
    ospath_normpath_vs_abspath()
    # properties
    ospath_properties()
    # tests
    ospath_tests()