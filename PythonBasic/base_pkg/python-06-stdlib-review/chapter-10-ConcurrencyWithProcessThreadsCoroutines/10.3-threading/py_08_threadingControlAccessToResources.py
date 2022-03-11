import sys, threading, random, time, logging
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def threading_lock():
    class Counter:
        def __init__(self, start=0):
            self.lock = threading.Lock()
            self.value = start

        def increment(self):
            logging.debug('Waiting for lock')
            self.lock.acquire()
            try:
                logging.debug('Acquired lock')
                self.value = self.value + 1
            finally:
                self.lock.release()

    def worker(c):
        for _ in range(2):
            pause = random.random()
            logging.debug('Sleeping %0.02f', pause)
            time.sleep(pause)
            c.increment()
        logging.debug('Done')

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    counter = Counter()
    for _ in range(2):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()

    logging.debug('Waiting for worker threads')
    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('Counter: %d', counter.value)

    pass


@addBreaker
def threading_lock_nobloc():
    def lock_holder(lock):
        logging.debug('Starting')
        while True:
            lock.acquire()
            try:
                logging.debug('Holding')
                time.sleep(0.5)
            finally:
                logging.debug('Not holding')
                lock.release()
            time.sleep(0.5)

    def worker(lock):
        logging.debug('Starting')
        num_tries = 0
        num_acquires = 0
        while num_acquires < 3:
            time.sleep(0.5)
            logging.debug('Trying to acquire')
            have_it = lock.acquire(0)
            try:
                num_tries += 1
                if have_it:
                    logging.debug('Iteration %d: Acquired', num_tries)
                    num_acquires += 1
                else:
                    logging.debug('Iteration %d: Not acquired', num_tries)
            finally:
                if have_it:
                    lock.release()
        logging.debug('Done after %d iterations', num_tries)

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    lock = threading.Lock()
    holder = threading.Thread(
        target=lock_holder,
        args=(lock,),
        name='LockHolder',
        daemon=True,
    )
    holder.start()
    worker = threading.Thread(
        target=worker,
        args=(lock,),
        name='Worker',
    )
    worker.start()
    pass

@addBreaker
def threading_lock_reacquire():
    lock = threading.Lock()
    print('First try :', lock.acquire())
    print('Second try:', lock.acquire(0))
    pass

@addBreaker
def threading_rlock():
    lock = threading.RLock()
    print('First try :', lock.acquire())
    print('Second try:', lock.acquire(0))
    pass

@addBreaker
def threading_lock_with():
    def worker_with(lock):
        with lock:
            logging.debug('Lock acquired via with')
            
    def worker_no_with(lock):
        lock.acquire()
        try:
            logging.debug('Lock acquired directly')
        finally:
            lock.release()

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    lock = threading.Lock()
    w = threading.Thread(target=worker_with, args=(lock,))
    nw = threading.Thread(target=worker_no_with, args=(lock,))
    w.start()
    nw.start()
    pass


if __name__ == "__main__":
    ### true `lock`
    threading_lock()
    """
    Normal Lock objects cannot be acquired more than once, even by the same thread. 
    If a lock is accessed by more than one function in the same call chain, 
    undesirable side effects may occur.
    """
    threading_lock_nobloc()
    ### re-entrant locks
    threading_lock_reacquire()
    ### `reacquire` the lock, use an RLock instead.
    threading_rlock()
    ### locks as context managers. 69 nice
    threading_lock_with()
