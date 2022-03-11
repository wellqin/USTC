import multiprocessing, time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s'
)

def slow_worker():
    logging.debug('starting worker')
    time.sleep(.1)
    logging.debug('finished worker')
    pass

if __name__ == "__main__":
    """
    although it is better to use the `poison pill` method of signaling to a process that it should exit.

    if a process apears hung or deadlocked, it can be useful to be able to kill it forcibly using `terminate()`
    """
    p = multiprocessing.Process(
        target=slow_worker,
    )
    logging.debug(f'BEFORE    : {p} {p.is_alive()}')
    p.start()
    logging.debug(f'DURING    : {p} {p.is_alive()}')
    ### ! it's important to `join()` AFTER `terminate()` it. 
    ### ! so as to give the process management code enough time to update the status of the object to reflect the termination
    p.terminate()
    logging.debug(f'TERMINATED: {p} {p.is_alive()}')
    p.join()
    logging.debug(f'JOINED    : {p} {p.is_alive()}')
    pass