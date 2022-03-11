import sys, glob
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def glob_escape():
    # ! sample code in the book P360 is NOT gonna work
    # ! winOS doesn't give a f*ck
    specials = '+-['

    for char in specials:
        pattern = 'dir/*' + glob.escape(char) + '.txt'
        print('Searching for: {!r}'.format(pattern))
        for name in sorted(glob.glob(pattern)):
            print(name)
        print()

    pass


if __name__ == "__main__":
    glob_escape()