import heapq, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from py_01_heapqData import data
from py_02_heapqShowtree import show_tree

@addBreaker
def heapq_heappush():
    # create a heap
    heap = []
    print('random: ', data)    
    print()
    for n in data:
        print('add {:>3}'.format(n))
        heapq.heappush(heap, n)
        show_tree(heap)

@addBreaker
def heapq_heapify():
    print('random   :', data)
    # heapq.heapify() is in-place modification
    heapq.heapify(data)
    print('heapified:')
    show_tree(data)

@addBreaker
def heapq_heappop():
    print('random   :', data)
    heapq.heapify(data)
    print('heapified:')
    show_tree(data)
    print()
    for _ in range(2):
        smallest = heapq.heappop(data)
        print('pop  {:>3}:'.format(smallest))
        show_tree(data)

@addBreaker
def heapq_heapreplace():
    data = [19, 9, 4, 10, 11]
    heapq.heapify(data)
    print('start:')
    show_tree(data)

    for n in [0, 13]:
        smallest = heapq.heapreplace(data, n)
        print('replace {:>2} with {:>2}:'.format(smallest, n))
        show_tree(data)

@addBreaker
def heapq_extremes():
    data = [19, 9, 4, 10, 11]
    print('all       :', data)
    print('3 largest :', heapq.nlargest(3, data))
    print('from sort :', list(reversed(sorted(data)[-3:])))
    print('3 smallest:', heapq.nsmallest(3, data))
    print('from sort :', sorted(data)[:3])

@addBreaker
def heapq_merge():
    import random, itertools
    random.seed(2016)
    data = []
    # generate some random integers for further usage
    for _ in range(4):
        new_data = list(random.sample(range(1, 101), 5))
        new_data.sort()
        data.append(new_data)
    for i, d in enumerate(data):
        print('{}: {}'.format(i, d))
    # combing several sorted sequences into one new sequence is easy for 'small' data sets ..
    print('\nMerge by itertools.chain()')
    for i in list(sorted(itertools.chain(*data))):
        print(i, end=' ')
    # heapq.merge() does it more efficiently
    print('\nMerge by heapq.merge()')
    for i in heapq.merge(*data):
        print(i, end=' ')

def main():
    # create a heap using heapq.heappush(data)
    heapq_heappush()
    # if data is in memory alrdy, using heapq.heapify(data) is more efficient
    heapq_heapify()
    # remove the element with the lowest value by using heapq.heappop()
    heapq_heappop()
    # replace an existing value with a new value by using heapq.heapreplace()
    heapq_heapreplace()
    # heapq also has an abitlity to examine the largest or smallest values in an iterable. just like large(array, k) in VB
    # heapq.nlarge() vs sorted()
    heapq_extremes()
    # combing several sorted sequences into one new sequence is easy for 'small' data sets, using ```list(sorted(itertools.chain(*data)))```
    # heapq.merge() does it more efficiently
    heapq_merge()

if __name__ == "__main__":
    main()