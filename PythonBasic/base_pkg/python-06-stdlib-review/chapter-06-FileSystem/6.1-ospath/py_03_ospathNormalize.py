import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def ospath_normpath():
    PATHS = [
        'one//two//three',
        'one/./two/./three',
        'one/../alt/two/three',
    ]
    
    for path in PATHS:
        print('{!r:>22} : {!r}'.format(path, os.path.normpath(path)))
    
    return

### P336 or P374

if __name__ == "__main__":
    # normpath()
    ospath_normpath()