import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_randint():
    s, e = 1, 100
    print('[{}, {}]:'.format(s, e), end=' ')
    for _ in range(10):
        print(random.randint(s, e), end=' ')
    s, e = -5, 5
    print('\n[{}, {}]:'.format(s, e), end=' ')
    for _ in range(3):
        print(random.randint(s, e), end=' ')
    
@addBreaker
def random_randrange():
    s, e, step = 1, 100, 5
    print('[{}, {}]:'.format(s, e), end=' ')
    for _ in range(10):
        print(random.randrange(s, e, step), end=' ')    

if __name__ == "__main__":
    # using randint() if wanted random integers between x <= n <=y(?). bingo
    random_randint()
    # using randrange() if wanted more controls, and not including ubound
    random_randrange()