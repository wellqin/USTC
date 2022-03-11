import sys, mmap
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def mmap_write():
    import shutil, os
    os.chdir(os.path.dirname(__file__))
    # copy the example file
    shutil.copyfile('lorem.txt', 'lorem_copy.txt')

    word = b'consectetuer'
    rved = word[::-1]
    print('looking for      :', word)
    print('replacing with   :', rved)
    with open('lorem_copy.txt', 'r+') as f:
        with mmap.mmap(f.fileno(), 0) as m:
            print('\nBEFORE: \n{}'.format(m.readline().rstrip()))
            m.seek(0)   # rewind
            
            loc = m.find(word)
            m[loc: loc + len(word)] = rved
            m.flush()

            m.seek(0)   # rewind
            print('\nAFTER : \n{}'.format(m.readline().rstrip()))

            f.seek(0)   # rewind
            print('\nFile  : \n{}'.format(f.readline().rstrip()))

if __name__ == "__main__":
    mmap_write()