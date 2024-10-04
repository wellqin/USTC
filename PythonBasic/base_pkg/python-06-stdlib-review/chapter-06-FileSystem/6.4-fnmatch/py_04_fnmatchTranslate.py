import sys, fnmatch
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def fnmatch_translate():
    pattern = 'fnmatch_*.py'
    print('Pattern  :', pattern)
    print('Regex    :', fnmatch.translate(pattern))

    pass

if __name__ == "__main__":
    # nice, beyond default setting under hood, u can explicitly translate regex 
    fnmatch_translate()