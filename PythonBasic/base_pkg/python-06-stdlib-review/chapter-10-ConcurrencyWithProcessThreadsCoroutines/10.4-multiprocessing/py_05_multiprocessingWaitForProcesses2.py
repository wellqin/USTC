import multiprocessing, time, sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
)

def daemon():
    name = multiprocessing.current_process().name
    logging.debug(f'Starting: {name}')
    time.sleep(2)
    logging.debug(f'Exiting : {name}')
    pass

def non_daemon():
    name = multiprocessing.current_process().name
    logging.debug(f'Starting: {name}')
    logging.debug(f'Exiting : {name}')
    pass


if __name__ == "__main__":
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
    )
    d.daemon = True
    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    n.start()

    """
    By default, join() blocks indefinitely. 
    
    Alternatively, a timeout argument (a float representing
    the number of seconds to wait for the process to become inactive) may be passed
    to the module. If the process does not complete within the timeout period, join() returns
    anyway.
    """
    d.join(1)
    logging.debug(f'd.is_alive() = {d.is_alive()}')
    n.join()
    pass