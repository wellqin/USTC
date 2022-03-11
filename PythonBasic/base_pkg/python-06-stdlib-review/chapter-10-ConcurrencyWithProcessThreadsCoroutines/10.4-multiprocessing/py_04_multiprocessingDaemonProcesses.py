"""

+----------------------+------------------------+---------------------+
| attr                 | threading              | multiprocessing     |
+======================+========================+=====================+
| Daemon               | YES                    | YES                 |
+----------------------+------------------------+---------------------+
| Name                 | YES                    | YES                 |
+----------------------+------------------------+---------------------+
| Wait                 | YES                    | YES                 |
+----------------------+------------------------+---------------------+

"""


import multiprocessing, time, sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
)

def daemon():
    p = multiprocessing.current_process()
    logging.debug(f'Starting: {p.name},{p.pid}')
    sys.stdout.flush()
    time.sleep(2)
    logging.debug(f'Exiting : {p.name},{p.pid}')
    sys.stdout.flush()
    pass

def non_daemon():
    p = multiprocessing.current_process()
    logging.debug(f'Starting: {p.name},{p.pid}')
    sys.stdout.flush()
    logging.debug(f'Exiting : {p.name},{p.pid}')
    sys.stdout.flush()
    pass


if __name__ == "__main__":
    """
    ! The output does not include the “Exiting” message from the daemon process, since all
    of the non-daemon processes (including the main program) exit before the daemon process
    wakes up from its 2-second sleep.

    The daemon process is terminated automatically before the main program exits, which
    avoids the case in which orphaned processes are left running. 
    
    This behavior can be verified by looking for the process ID value that is printed when the program runs, and then checking
    for that process with a command such as `ps`
    """
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True
    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    d.start()
    time.sleep(1)
    n.start()
    pass