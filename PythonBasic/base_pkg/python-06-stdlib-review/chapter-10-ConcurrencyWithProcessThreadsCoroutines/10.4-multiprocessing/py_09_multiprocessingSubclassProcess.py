"""
the simplest way to start a job in a separate process is to use `Process` 
and pass a target function

it is also possible to use a custom sublcass.

::wink::
Doesn't it sound like a decorator? 
"""

import multiprocessing
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s, pid:%(process)6s, %(message)s',
)

class Worker(multiprocessing.Process):
    def run(self):
        logging.debug(f'In {self.name}')
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()
