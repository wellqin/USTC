"""
deque == double-ended queue
! the more commonly used **stacks** and **queues** are degenerated forms of deques. 
"""

import collections, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def collections_deque_create():
    d = collections.deque('abcdefg')
    print('Deque     :', d)
    print('Length    :', len(d))
    print('Left end  :', d[0])
    print('Right end :', d[-1])
    
    d.remove('c')
    print('removed(c):', d)

@addBreaker
def collections_deque_populate():
    # add to the right
    d1 = collections.deque()
    d1.extend('abcdefg')
    print('extend       :', d1)
    d1.append('h')
    print('append       :', d1)
    # add to the left
    d2 = collections.deque()
    d2.extendleft(range(6))
    print('extendleft   :', d2)
    d2.appendleft(6)
    print('appendleft   :', d2)

@addBreaker
def collections_deque_consume():
    d1 = collections.deque('abcdefg')
    print('\nFrom the right :', end='')
    while True:
        try:
            print(d1.pop(), end=' ')
        except IndexError:
            break
    print('\nFrom the left  :', end='')
    d2 = collections.deque(range(6))
    while True:
        try:
            print(d2.popleft(), end=' ')
        except IndexError:
            break

@addBreaker
def collections_deque_both_ends():
    import threading, time
    def burn(direction, nextSource):
        while True:
            try:
                next = nextSource()
            except IndexError:
                break
            else:
                print('{:>8}: {}'.format(direction, next))   
                time.sleep(.1)
        return

    candle = collections.deque(range(5))
    left   = threading.Thread(target=burn, args=('Left', candle.popleft))
    right  = threading.Thread(target=burn, args=('Right', candle.pop))
    left.start()
    right.start()
    left.join()
    right.join()

@addBreaker
def collections_deque_rotate():
    # ? image it likes majo ..
    d = collections.deque(range(10))
    print('Normal         :', d)
    d = collections.deque(range(10))
    d.rotate(2)
    print('Right rotation :', d)
    d = collections.deque(range(10))
    d.rotate(-2)
    print('Left rotation  :', d)

@addBreaker
def collections_deque_maxlen():
    import random
    random.seed(1)
    d1 = collections.deque(maxlen=3)
    d2 = collections.deque(maxlen=3)

    for _ in range(5):
        n = random.randint(0, 100)
        print('n = ', n)
        d1.append(n)
        d2.appendleft(n)
        print('d1:', d1)
        print('d2:', d2)


def main():
    # first impression. creating
    collections_deque_create()
    # populating a deque
    collections_deque_populate()
    # consuming
    collections_deque_consume()
    # deque is thread-safe, it's ok to consume from both ends at the same time
    collections_deque_both_ends()
    # rotating
    collections_deque_rotate()
    # set up maxlen
    collections_deque_maxlen()

if __name__ == "__main__":
    main()