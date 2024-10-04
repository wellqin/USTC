import sys, threading
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def threading_simple():
    def worker():
        """thread worker function"""
        print('Worker')

    threads = []

    for _ in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    pass

@addBreaker
def threading_simpleargs():
    def worker(num):
        """thread worker function"""
        print('Woker: %s' % num)
    
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    pass

if __name__ == "__main__":
    ### simple no-args function
    threading_simple()
    ### simple function with one arg
    threading_simpleargs()
