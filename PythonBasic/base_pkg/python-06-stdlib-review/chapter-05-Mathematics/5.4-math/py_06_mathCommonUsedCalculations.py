import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_fsum():
    values = [0.1] * 10
    print('Input values :', values)
    print('sum()        : {:.20f}'.format(sum(values)))
    s = 0.0
    for i in values:
        s += i
    print('for-loop     : {:.20f}'.format(s))
    print('math.fsum()  : {:.20f}'.format(math.fsum(values)))

@addBreaker
def math_factorial_vs_gamma():
    print('math.factorial(n) == n! :')
    for i in [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.1]:
        try:
            print('{:2.0f} {:6.0f}'.format(i, math.factorial(i)))
        except ValueError as err:
            print('Error computing factorial({}): {}'.format(i, err))   
    print('\nmath.gamma(n) == (n-1)! :')
    for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]:
        try:
            print('{:2.0f} {:6.0f}'.format(i, math.gamma(i)))
        except ValueError as err:
            print('Error computing gamma({}): {}'.format(i, err))   

@addBreaker
def math_lgamma():
    for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]:
        try:
            print('{:2.1f} {:.20f} {:.20f}'.format(
                i,
                math.lgamma(i),
                math.log(math.gamma(i)))
            )
        except ValueError as err:
            print('Error computing lgamma({}): {}'.format(i, err))
   
@addBreaker
def math_fmod():
    print('{:^4} {:^4} {:^5} {:^5}'.format('x', 'y', '%', 'fmod'))
    print('{:-^4} {:-^4} {:-^5} {:-^5}'.format('-', '-', '-', '-'))
    INPUTS = [
        (5, 2),
        (5, -2),    
        (-5, 2),
    ]
    for x, y in INPUTS:
        print('{:4.1f} {:4.1f} {:5.2f} {:5.2f}'.format(
                x,
                y,
                x % y,
                math.fmod(x, y),
        ))
  
@addBreaker
def math_gcd():
    print(math.gcd(10, 8))
    print(math.gcd(10, 0))
    print(math.gcd(50, 225))
    print(math.gcd(11, 9))
    print(math.gcd(0, 0))


if __name__ == "__main__":
    # math.fsum() retains fedility of floating-point value
    math_fsum()
    # factorial() .. fml, i had invented wheels..
    # and gamma() ..
    math_factorial_vs_gamma()
    # logarithm gamma
    math_lgamma()
    # mod() % vs fmod()
    math_fmod()
    # gcd
    math_gcd()
