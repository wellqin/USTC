import sys, threading, time, logging
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def threading_subclass():
    class MyThread(threading.Thread):
        def run(self):
            logging.debug('running')

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    for _ in range(5):
        t = MyThread()
        t.start()

    pass

@addBreaker
def threading_subclass_args():
    class MyThreadWithArgs(threading.Thread):
        def __init__(self, group=None, target=None, name=None,
            args=(), kwargs=None, *, daemon=None):
            super().__init__(group=group, target=target, name=name,
            daemon=daemon)
            self.args = args
            self.kwargs = kwargs
        def run(self):
            logging.debug('running with %s and %s', self.args, self.kwargs)

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    for i in range(5):
        t = MyThreadWithArgs(args=(i,), kwargs={'a': 'A', 'b': 'B'})
        t.start()
    pass

if __name__ == "__main__":
    ### the default behavior of `Thread.run()` 
    ### which in turn calls the target function passed to the constructor.
    ### anyway, u may override `run()` behavior
    threading_subclass()
    ### by default, `Thread` obj's args and kwargs are privite
    ### you may make them easy to access by user-defined subclass
    threading_subclass_args()