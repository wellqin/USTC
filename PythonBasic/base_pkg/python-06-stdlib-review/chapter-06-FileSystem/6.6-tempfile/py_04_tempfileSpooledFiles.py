import sys, tempfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tempfile_SpooledTemporaryFile():
    with tempfile.SpooledTemporaryFile(
        max_size=100,
        mode='w+t',
        encoding='utf8'
    ) as temp:
        print('temp: {!r}'.format(temp))
        
        for _ in range(3):
            temp.write('This line is repeated over and over .\n')
            print(temp._rolled, temp._file)
    pass

@addBreaker
def tempfile_SpooledTemporaryFile_explicit():

    with tempfile.SpooledTemporaryFile(
        max_size=100,
        mode='w+t',
        encoding='utf8'
    ) as temp:
        for _ in range(3):
            temp.write('This line is repeated over and over.\n')
            print(temp._rolled, temp._file)
        print('rolling over by using rollover()')
        temp.rollover()
        print(temp._rolled, temp._file)
    pass


if __name__ == "__main__":
    # concept
    # SpooledTemporaryFile() creates a file in memory ..
    # so it makes sense
    tempfile_SpooledTemporaryFile()
    # explicitly rollover using rollover() or fileno()
    tempfile_SpooledTemporaryFile_explicit()