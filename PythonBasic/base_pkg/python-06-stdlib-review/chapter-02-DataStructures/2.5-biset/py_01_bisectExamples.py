import bisect, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def bisect_find_index_and_insert():
    import random
    # a series of random numbers
    random.seed(2020)
    values = random.sample(range(1, 101), 13)
    values.append(57) # intends to append a duplicate value 57
    print('New Pos Contents')
    print('--- --- --------')
    l = []
    for value in values:
        # find index
        position = bisect.bisect(l, value)
        # insert and sort
        bisect.insort(l, value)
        print('{:3} {:3}'.format(value, position), l)

@addBreaker
def bisect_handle_duplicates():
    import random
    # a series of random numbers
    random.seed(2020)
    values = random.sample(range(1, 101), 13)
    values.append(57) # intends to append a duplicate value 57
    print('New Pos Contents')
    print('--- --- --------')
    # use bisect_left and insort_left
    l = []
    for value in values:
        # find index
        position = bisect.bisect_left(l, value)
        # insert and sort
        bisect.insort_left(l, value)
        print('{:3} {:3}'.format(value, position), l)
        
def main():
    # bisect, find index, and insert while maintaining lists in sorted order
    # when to use bisect? for long lists, significant time and memory savings can be achieved using bisect.insort()
    bisect_find_index_and_insert()
    # if a sequence has duplicate values ..
    # finding index via bisect_left() or bisect_right(), insert via insort_left() or insort_right()
    bisect_handle_duplicates()

if __name__ == "__main__":
    main()