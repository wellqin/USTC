import logging, time, os
from concurrent import futures
import signal 

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s'
)

with futures.ProcessPoolExecutor(max_workers=2) as ex:
    logging.debug('getting the pid for one worker')
    f1 = ex.submit(os.getpid)
    pid1 = f1.result()

    logging.debug('killing process {}'.format(pid1))
    os.kill(pid1, signal.SIG_IGN)

    logging.debug('submitting another task')
    f2 = ex.submit(os.getpid)
    try:
        pid2 = f2.result()
    except futures.process.BrokenProcessPool as e:
        logging.debug('could not start new tasks: {}'.format(e))

"""
fck this AtrributeError: can't pickle balabala ..
"""