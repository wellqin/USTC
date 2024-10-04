import sys, threading, time, logging
sys.path.append('.')
from pkg.breaker import addBreaker


@addBreaker
def threading_event():
    def wait_for_event(e):
        """Wait for the event to be set before doing anything"""
        logging.debug('wait_for_event starting')
        event_is_set = e.wait()
        logging.debug('event set: %s', event_is_set)
    def wait_for_event_timeout(e, t):
        """Wait t seconds and then timeout"""
        while not e.is_set():
            logging.debug('wait_for_event_timeout starting')
            event_is_set = e.wait(t)
            logging.debug('event set: %s', event_is_set)
            if event_is_set:
                logging.debug('processing event')
            else:
                logging.debug('doing other work')

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    e = threading.Event()
    t1 = threading.Thread(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    t1.start()
    t2 = threading.Thread(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2),
    )
    t2.start()
    logging.debug('Waiting before calling Event.set()')
    time.sleep(0.3)
    e.set()
    logging.debug('Event is set')
    pass


if __name__ == "__main__":
    """
    although the point of using multiple threads is to run separate operations concurrently,
    sometimes it is important to be able to synchronize the operations in two or more threads
    
    * Event objects are a simple way to communicate between threads safely.
    ? delegate? probable

    * Event objects -- set(), clear(), wait()
    """
    ### `an event` manages an internal flag that
    ### callers can control with the `set()` and `clear()` methods.
    ### other `thread` can use `wait()` to pause until the flag is set.
    ### ! effectively blocking progress until those threads are allowed to continue
    threading_event()
