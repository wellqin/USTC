import sys, tempfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tempfile_NamedTemporaryFile_args():
    # ! formula= `dir + prefix + random + suffix`
    # ? why?
    # * including a predictable portion in the name makes it possible to find the file and examine it for debugging purposes
    with tempfile.NamedTemporaryFile(
        suffix='_suffix',
        prefix='prefix_',
        dir='C:/Users/5106001995/AppData/Local/Temp'
    ) as temp:
        print('temp:')
        print(' ', temp)
        print('temp.name:')
        print(' ', temp.name)
    pass

if __name__ == "__main__":
    tempfile_NamedTemporaryFile_args()