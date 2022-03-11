import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_trig():
    print('{:^7} {:^7} {:^7} {:^7} {:^7}'.format('Degrees', 'Radians', 'Sine', 'Cosine', 'Tangent'))
    print('{:-^7} {:-^7} {:-^7} {:-^7} {:-^7}'.format('-', '-', '-', '-', '-'))
    fmt = '{:7.2f} {:7.2f} {:7.2f} {:7.2f} {:7.2f}'
    for deg in range(0, 361, 30):
        rad = math.radians(deg)
        if deg in (90, 270):
            t = float('inf')
        else:
            t = math.tan(rad)
        print(fmt.format(deg, rad, math.sin(rad), math.cos(rad), t))

@addBreaker
def math_hypot():
    print('{:^7} {:^7} {:^10}'.format('X', 'Y', 'Hypotenuse'))
    print('{:-^7} {:-^7} {:-^10}'.format('', '', ''))
    POINTS = [
        # Simple points
        (1, 1),
        (-1, -1),
        (math.sqrt(2), math.sqrt(2)),
        (3, 4), # 3-4-5 triangle
        # On the circle
        (math.sqrt(2) / 2, math.sqrt(2) / 2), # pi/4 rads
        (0.5, math.sqrt(3) / 2), # pi/3 rads
    ]
    for x, y in POINTS:   
        h = math.hypot(x, y)
        print('{:7.2f} {:7.2f} {:7.2f}'.format(x, y, h))

@addBreaker
def math_distance_2_points():
    print('{:^8} {:^8} {:^8} {:^8} {:^8}'.format(
    'X1', 'Y1', 'X2', 'Y2', 'Distance',
    ))
    print('{:-^8} {:-^8} {:-^8} {:-^8} {:-^8}'.format(
    '', '', '', '', '',
    ))
    POINTS = [
        ((5, 5), (6, 6)),    
        ((-6, -6), (-5, -5)),
        ((0, 0), (3, 4)), # 3-4-5 triangle
        ((-1, -1), (2, 3)), # 3-4-5 triangle
    ]
    for (x1, y1), (x2, y2) in POINTS:
        x = x1 - x2
        y = y1 - y2
        h = math.hypot(x, y)
        print('{:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f}'.format(
        x1, y1, x2, y2, h,
        ))

@addBreaker
def math_invert_trig():
    for r in [0, 0.5, 1]:
        print('arcsine({:.1f}) = {:5.2f}'.format(r, math.asin(r)))
        print('arccosine({:.1f}) = {:5.2f}'.format(r, math.acos(r)))
        print('arctangent({:.1f}) = {:5.2f}'.format(r, math.atan(r)))
        print()
        

if __name__ == "__main__":
    # sine, cosine
    math_trig()
    # hypotenues
    math_hypot()
    # distance of two points
    math_distance_2_points()
    # yeah, the world really loves pairs :^)
    # invert trig, there we go!
    math_invert_trig()