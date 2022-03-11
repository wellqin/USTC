import sys, threading, logging, time
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def threading_timer():
    def delayed():
        logging.debug('worker running')

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    t1 = threading.Timer(0.3, delayed)
    t1.setName('t1')
    t2 = threading.Timer(0.3, delayed)
    t2.setName('t2')

    logging.debug('starting timers')
    t1.start()
    t2.start()
    logging.debug('waiting before canceling %s', t2.getName())
    time.sleep(0.2)
    logging.debug('canceling %s', t2.getName())
    t2.cancel()
    logging.debug('done')
    pass

if __name__ == "__main__":
    ### a reason to subclass `Thread` is provided by `Timer`,
    ### which is also included in threading.
    ### ! A `timer` starts its work after a delay, and can be canceled at any point within that delay time period by using `thread.cancel()`
    threading_timer()
