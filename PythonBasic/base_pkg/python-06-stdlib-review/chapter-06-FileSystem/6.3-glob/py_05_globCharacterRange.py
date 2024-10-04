import sys, glob
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def glob_charrange():
    for name in glob.glob('dir/*[0-9].*'):
        print(name)
    pass

if __name__ == "__main__":
    # character range in regex, wow
    glob_charrange()
