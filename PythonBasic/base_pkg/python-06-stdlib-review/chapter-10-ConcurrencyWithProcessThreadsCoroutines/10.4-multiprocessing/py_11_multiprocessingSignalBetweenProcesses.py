import multiprocessing, time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
)

def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('wait_for_event: starting')
    e.wait()
    logging.debug(f'wait_for_event: e.is_set()-> {e.is_set()}')
def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    logging.debug('wait_for_event_timeout: starting')
    e.wait(t)
    logging.debug(f'wait_for_event_timeout: e.is_set()-> {e.is_set()}')

if __name__ == '__main__':
    ### some concepts as with `Threading`
    # ! yah, the concept of delegate in C#
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    w1.start()
    w2 = multiprocessing.Process(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2),
    )
    w2.start()
    logging.debug('main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('main: event is set')
