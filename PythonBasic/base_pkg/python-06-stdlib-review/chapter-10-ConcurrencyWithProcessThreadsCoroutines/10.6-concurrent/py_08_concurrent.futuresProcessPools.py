import logging, os
from concurrent import futures

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(process)d %(message)s')

def futures_process_pool_map():
    def task(n):
        return (n, os.getpid())

    with futures.ProcessPoolExecutor(max_workers=2) as ex:
        results = ex.map(task, range(5, 0, -1))
    """
    ! AttributeError: Can't pickle local object 'futures_process_pool_map.<locals>.task'
    
    The problem is that multiprocessing must pickle things to sling them among processes, 
    and bound methods are not picklable. 
    The workaround (whether you consider it "easy" or not;-) is to 
    add the infrastructure to your program to allow such methods to be pickled, 
    registering it with the copy_reg standard library method.    

    In theory, python can't pickle functions. (for details, see Can't pickle Function)
    In practice, python pickles a function's name and module so that passing a function will work. 

    Pool needs to pickle (serialize) everything it sends to its worker-processes (IPC). 
    Pickling actually only saves the name of a function and unpickling requires re-importing the function by name. 
    For that to work, the function needs to be defined at the top-level, 
    nested functions won't be importable by the child and already trying to pickle them raises an exception (more).

    """
    for n, pid in results:
        logging.debug(f'ran task {n} in process {pid}')

"""
! a big problem here is we can't use "__main__" to run wrapped Process related functions.

! Q: why not?
* A: cuz, just like `multiprocessing` or `asyncio` "Process" obj 
* always has an extra protection on "__main__" to prevent recursive call.

! Q: why can it prevent recursive call?
* A: my guess is "main process" may affect this modules in low level implementation
"""
# if __name__ == "__main__":
#     futures_process_pool_map()

futures_process_pool_map()