import sys, glob
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def glob_asterisk():
    # ! NOT include files in subdir tho ..
    for name in sorted(glob.glob('dir/*')):
        print(name)

@addBreaker
def glob_sudir():
    print('Named explicitly:')
    for name in sorted(glob.glob('dir/subdir/*')):
        print(' {}'.format(name))
    print('Named with wildcard:')
    for name in sorted(glob.glob('dir/*/*')):
        print(' {}'.format(name))
    

if __name__ == "__main__":
    # hmm, wildcard *, subdir files are NOT reachable
    glob_asterisk()
    # wanna reach subdir files, understand glob.glob() behavior first
    glob_sudir()