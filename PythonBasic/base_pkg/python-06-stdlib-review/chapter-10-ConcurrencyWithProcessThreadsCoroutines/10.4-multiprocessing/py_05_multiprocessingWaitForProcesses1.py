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
    time.sleep(1)
    n.start()

    d.join()
    n.join()
    pass