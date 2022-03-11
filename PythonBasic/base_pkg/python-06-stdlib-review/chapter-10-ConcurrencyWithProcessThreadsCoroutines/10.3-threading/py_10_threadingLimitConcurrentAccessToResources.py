import sys, threading, time, logging, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def threading_semaphore():
    class ActivePool:
        def __init__(self):
            super(ActivePool, self).__init__()
            self.active = []
            self.lock = threading.Lock()
        def makeActive(self, name):
            with self.lock:
                self.active.append(name)
                logging.debug('Running: %s', self.active)
        def makeInactive(self, name):
            with self.lock:
                self.active.remove(name)
                logging.debug('Running: %s', self.active)

    def worker(s, pool):
        logging.debug('Waiting to join the pool')
        with s:
            name = threading.current_thread().getName()
            pool.makeActive(name)
            time.sleep(0.1)
            pool.makeInactive(name)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s (%(threadName)-2s) %(message)s',
    )
    pool = ActivePool()
    s = threading.Semaphore(2)
    for i in range(4):
        t = threading.Thread(
            target=worker,
            name=str(i),
            args=(s, pool),
        )
        t.start()
    pass

if __name__ == "__main__":
    """
    Sometimes it is useful to allow more than one worker access to a resource at a time,
    while still limiting the overall number.

    For example, a connection pool might support a fixed number of simultaneous connection,
    or a network application might support a fixed number of concurrent downloads.

    A `semaphore` is one way to manage those connections
    
    A real resource pool would allocate a connection or 
    some other value to the newly active thread,
    and reclaim the value when the thread is done.
    """
    threading_semaphore()