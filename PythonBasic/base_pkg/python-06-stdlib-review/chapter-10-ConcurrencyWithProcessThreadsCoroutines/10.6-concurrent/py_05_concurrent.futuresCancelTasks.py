import logging, time
from concurrent import futures

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(threadName)-22s %(message)s')

def futures_future_callback():
    def task(n):
        logging.debug(f'{n}: sleeping')
        time.sleep(.5)
        logging.debug(f'{n}: done')
        return n / 10

    def done(fn):
        if fn.cancelled():
            logging.debug(f'{fn.arg}: cancelled')
        elif fn.done():
            error = fn.exception()
            if error:
                logging.debug(f'{fn.arg}: error returned')
        else:
            result = fn.result()
            logging.debug(f'result: {result}')
    
    ex = futures.ThreadPoolExecutor(max_workers=2)
    logging.debug('main: starting')
    tasks = []
    for i in range(10, 0, -1):
        logging.debug(f'main: submitting {i}')
        f = ex.submit(task, i)
        """
        ? Q: wtf is this line? commentout. 
        # * A: aha, got it. it merely likes naming a `Future` object, 
          *    just like naming a thread in `threading` or a process in `multiprocessing`

        ? Q: review: what is the concept of `Future` in Python's concurrency?
        * A: an imcompleted event/job/task
        """
        f.arg = i 
        # * aha, just like `threading` or `multiprocessing`, registers callback onto a Future object.
        f.add_done_callback(done)
        tasks.append((i, f))
    for i, t in reversed(tasks):
        """
        wait one second
        ? what the fking difference btwn f.cancel() and f.cancelled()?
        +-------------+--------------------------------------------------------------+-----------------------------------------------------+                                                                               
        | diff
        +-------------+--------------------------------------------------------------+-----------------------------------------------------+                                                                               
        | what to do? | attempts to cancel the call.                                 | return True if the call was successfully cancelled. |
        +-------------+--------------------------------------------------------------+-----------------------------------------------------+                                                                               
        | how         | if the call is currently being executed or finished running  | N/A                                                 |
        |             | and cannot be cancelled then method will return False,       |                                                     |
        |             | otherwise the call will be cancelled and return True         |                                                     |
        +-------------+--------------------------------------------------------------+-----------------------------------------------------+                                                                               

        link: https://docs.python.org/3/library/concurrent.futures.html
        """
        if not t.cancel():
            logging.debug(f'main: did not cancel {i}')

if __name__ == "__main__":
    futures_future_callback()