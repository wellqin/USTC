import sys, mmap
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def mmap_write_copy():
    import shutil, os
    os.chdir(os.path.dirname(__file__))
    # copy the example of file
    shutil.copyfile('lorem.txt', 'lorem_copy.txt')

    word = b'consectetuer'
    rved = word[::-1]
    print('looking for      :', word)
    print('replacing with   :', rved)
    with open('lorem_copy.txt', 'r+') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY) as m:
            print('\nMemory BEFORE: \n{}'.format(m.readline().rstrip()))
            print('\nFile   BEFORE: \n{}'.format(f.readline().rstrip()))

            m.seek(0)   # rewind
            loc = m.find(word)
            m[loc: loc + len(word)] = rved
            # m.flush()

            m.seek(0)   # rewind
            print('\nMemory AFTER : \n{}'.format(m.readline().rstrip()))
            f.seek(0)   # rewind
            print('\nFile   AFTER : \n{}'.format(f.readline().rstrip()))

if __name__ == "__main__":
    # ! argument `access` == ACCESS_COPY, changes are NOT written to the file on disk
    # ! means file obj and mmap obj are separate instances.
    mmap_write_copy()