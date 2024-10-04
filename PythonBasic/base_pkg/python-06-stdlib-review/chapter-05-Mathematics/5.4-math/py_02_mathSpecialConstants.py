import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_special_constants():
    print('   π : {:.30f}'.format(math.pi))
    print('   e : {:.30f}'.format(math.e))
    print(' nan : {:.30f}'.format(math.nan))
    # ikr, decimal has this thing too
    print(' inf : {:.30f}'.format(math.inf))
    
    
    pass

if __name__ == "__main__":
    math_special_constants()