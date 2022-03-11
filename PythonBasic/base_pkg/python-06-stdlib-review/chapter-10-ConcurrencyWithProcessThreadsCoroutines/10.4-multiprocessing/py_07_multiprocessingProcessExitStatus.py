"""

Table: multiprocessing Exit Codes
+---------------+-------------------------------------------------------+
| Exit Code     | Meaning                                               |
+---------------+-------------------------------------------------------+
|  == 0         | No error was produced                                 |
+---------------+-------------------------------------------------------+
|  > 0          | The process had an error, and exited with that code   |
+---------------+-------------------------------------------------------+
|  < 0          | The process was killed with a signal of -1 * exitcode |
+---------------+-------------------------------------------------------+


"""



import multiprocessing, sys, time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(processName)s %(message)s',
)

def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('There was an error!')

def terminated():
    time.sleep(3)


if __name__ == '__main__':
    jobs  = []
    funcs = [
        exit_error,
        exit_ok,
        return_value,
        raises,
        terminated,
    ]
    
    for f in funcs:
        logging.debug(f'starting process for {f.__name__}')
        j = multiprocessing.Process(
            name=f.__name__,
            target=f,
        )
        jobs.append(j)
        j.start()

    jobs[-1].terminate()
    
    for j in jobs:
        j.join()
        logging.debug(f'{j.name:>15}.exitcode = {j.exitcode}')

    pass