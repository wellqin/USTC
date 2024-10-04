import sys, threading
sys.path.append('.')
from pkg.breaker import addBreaker
import time
import logging

@addBreaker
def threading_names():
    def worker():
        print(threading.current_thread().getName(), 'Starting')
        time.sleep(.2)
        print(threading.current_thread().getName(), 'Exiting')
    
    def my_service():
        print(threading.current_thread().getName(), 'Starting')
        time.sleep(.3)
        print(threading.current_thread().getName(), 'Exiting')

    t  = threading.Thread(name='my_service', target=my_service)
    w  = threading.Thread(name='worker', target=worker)
    w2 = threading.Thread(target=worker) # use default name

    w.start()
    w2.start()
    t.start()

    pass

@addBreaker
def threading_names_log():
    def worker():
        logging.debug('Starting')
        time.sleep(.2)
        logging.debug('Exiting')
    
    def my_service():
        logging.debug('Starting')
        time.sleep(.3)
        logging.debug('Exiting')
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )

    t  = threading.Thread(name='my_service', target=my_service)
    w  = threading.Thread(name='worker', target=worker)
    w2 = threading.Thread(target=worker)

    w.start()
    w2.start()
    t.start()
    
    
    pass


if __name__ == "__main__":
    """
    Using arguments to identify or name the thread is cumbersome and unnecessary
    
    Each `Thread` instance has a name with a default value 
    that can be changed as the thread is created.

    Naming threads is useful in server processes 
    in which multiple service threads handle different operations
    """
    # ? threading.current_thread() vs threading.currentThread()?
    threading_names()
    # thread names + logging
    threading_names_log()