"""
as with threads, a common use pattern for multiple processes is 
to divide a job up among several workers to run in parallel.

Effective use of multiple processes usually requires some communication between them. 
! communication overhead is O(n^2) tho ..
so that work can be divided and results can be aggregated.

A simple way to communicate between processes with `multiprocessing` 
is to use a `Queue` to pass messages back and forth.

Any object that can be serialized with `pickle` can pass through a `Queue`
? htf do i know which object can be serialized in the first place?

"""


import multiprocessing
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s, %(message)s'
)

class MyFancyClass:
    def __init__(self, name):
        self.name = name
    def do_something(self):
        proc_name = multiprocessing.current_process().name
        logging.debug(f'Doing something fancy in {proc_name} for {self.name}')

def worker(q):
    obj = q.get()
    obj.do_something()

if __name__ == "__main__":
    que = multiprocessing.Queue()
    p   = multiprocessing.Process(
        target=worker,
        args=(que,),
    )
    ### put jobs into the queue
    que.put(MyFancyClass('Fancy ZL'))
    # start processes
    p.start()
    # wait for the worker to finish.
    que.close()
    que.join_thread()
    p.join()
