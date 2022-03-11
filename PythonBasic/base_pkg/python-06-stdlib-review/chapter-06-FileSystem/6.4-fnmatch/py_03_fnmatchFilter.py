import sys, fnmatch
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def fnmatch_filter():
    import os, pprint
    pattern = 'fnmatch'
    print('Pattern  :', pattern)
    files= os.listdir('.')
    print('\nFolders & Files  :')
    pprint.pprint(files)
    print('\nMatches:')
    pprint.pprint(fnmatch.filter(files, pattern))
    pass

if __name__ == "__main__":
    fnmatch_filter()