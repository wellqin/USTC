import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_positive_negative_signs():
    print(math.fabs(-1.1))
    print(math.fabs(-0.0))
    print(math.fabs(0.0))
    print(math.fabs(1.1))
    pass

@addBreaker
def math_copysign():
    HEADINGS = ('f', 's', '< 0', '> 0', '= 0')
    print('{:^5} {:^5} {:^5} {:^5} {:^5}'.format(*HEADINGS))
    print('{:-^5} {:-^5} {:-^5} {:-^5} {:-^5}'.format(*(' ',) * 5))
    VALUES = [
        -1.0,
        0.0,
        1.0,
        float('-inf'),
        float('inf'),
        float('-nan'),
        float('nan'),
    ]
    for f in VALUES:
        s = int(math.copysign(1, f))
        print('{:5.1f} {:5d} {!s:5} {!s:5} {!s:5}'.format(f, s, f < 0, f > 0, f == 0))


if __name__ == "__main__":
    # good old friend, fabs() in C/C++
    math_positive_negative_signs()
    # copy signs
    math_copysign()