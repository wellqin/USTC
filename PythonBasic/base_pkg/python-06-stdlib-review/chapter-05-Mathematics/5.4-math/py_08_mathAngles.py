import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_radians():
    print('{:^7} {:^7} {:^7}'.format('Degrees', 'Radians', 'Expected'))
    print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))
    INPUTS = [
        (0, 0),
        (30, math.pi / 6),
        (45, math.pi / 4),
        (60, math.pi / 3),
        (90, math.pi / 2),
        (180, math.pi),
        (270, 3 / 2.0 * math.pi),
        (360, 2 * math.pi),
    ]
    for deg, expected in INPUTS:
        print('{:7d} {:7.2f} {:7.2f}'.format(deg, math.radians(deg), expected))

@addBreaker
def math_degrees():
    INPUTS = [
        (0, 0),
        (math.pi / 6, 30),
        (math.pi / 4, 45),
        (math.pi / 3, 60),
        (math.pi / 2, 90),
        (math.pi, 180),
        (3 * math.pi / 2, 270),
        (2 * math.pi, 360),
    ]
    print('{:^8} {:^8} {:^8}'.format('Radians', 'Degrees', 'Expected'))
    print('{:-^8} {:-^8} {:-^8}'.format('', '', ''))
    for rad, expected in INPUTS:
        print('{:8.2f} {:8.2f} {:8.2f}'.format(rad, math.degrees(rad), expected))


if __name__ == "__main__":
    # degrees -> radians
    math_radians()
    # degrees <- radians
    math_degrees()
    pass