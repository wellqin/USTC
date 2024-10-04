import sys, threading
sys.path.append('.')
from pkg.breaker import addBreaker
import time, logging

@addBreaker
def threading_daemon():
    def daemon():
        logging.debug('starting')
        time.sleep(.2)
        logging.debug('exiting')
    
    def non_daemon():
        logging.debug('starting')
        logging.debug('exiting')
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    
    d = threading.Thread(name='daemon', target=daemon, daemon=True)
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()
    pass

@addBreaker
def threading_daemon_join():
    def daemon():
        logging.debug('Starting')
        time.sleep(0.2)
        logging.debug('Exiting')

    def non_daemon():
        logging.debug('Starting')
        logging.debug('Exiting')

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    d = threading.Thread(name='daemon', target=daemon, daemon=True)
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()
    d.join()
    t.join()
    pass

@addBreaker
def threading_daemon_join_timeout():
    def daemon():
        logging.debug('Starting')
        time.sleep(0.2)
        logging.debug('Exiting')

    def non_daemon():
        logging.debug('Starting')
        logging.debug('Exiting')
        
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    d = threading.Thread(name='daemon', target=daemon, daemon=True) 
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()
    d.join(.1)
    print('d.isAlive()', d.isAlive())
    t.join()
    pass

if __name__ == "__main__":
    ### `daemon` guardian
    ### to mark a thread as a daemon, pass `daemon=True` when constructing it or call its `set_daemon()` method with True
    ### the default is for threads to not be daemons.
    ### ! Sometimes, however, programs spawn a thread as a daemon
    ### ! that runs w/o blocking the main program from exiting
    threading_daemon()
    ### To wait until a daemon thread has completed its work, use `join()` method
    ### ! ofc, `join()` blocks indefinitely.
    threading_daemon_join()
    ### ! sure, you may control number of seconds to wait for the thread to become inactive
    ### ! if the thread doesnt complete within the timeout period, `join()` return anyway
    threading_daemon_join_timeout()
