import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def see_diff_u_vs_r():
    # Python==2.* works differently though
    # Python==3.7
    print(sys.getsizeof('ciao'))
    print(sys.getsizeof(u'ciao'))

if __name__ == "__main__":
    see_diff_u_vs_r()