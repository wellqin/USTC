import sys, glob
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def glob_question():
    for name in glob.glob('dir/file?.txt'):
        print(name)
    pass

if __name__ == "__main__":
    # oh lala, enjoy regex power again!
    glob_question()