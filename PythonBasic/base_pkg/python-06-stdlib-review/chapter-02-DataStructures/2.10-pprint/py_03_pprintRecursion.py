import pprint, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def pprint_recursion():
    local_data = list('ab12')
    local_data.append(local_data)
    print('id(local_data) =>', id(local_data))
    pprint.pprint(local_data)

if __name__ == "__main__":
    pprint_recursion()