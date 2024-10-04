import logging, time
from concurrent import futures

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s'
)

def futures_future_callback():
    def task(n):
        logging.debug(f'{n}: sleeping')
        time.sleep(.5)
        logging.debug(f'{n}: done')
        return n / 10
    
    def done(fn):
        """
        ofc, an task have many status: (create), done, cancelled, exception
        """
        if fn.cancelled():
            logging.debug(f'{fn.arg}: canceled')
        elif fn.done():
            error = fn.exception()
            if error:
                logging.debug(f'{fn.arg}: error returned: {error}')
        else:
            result = fn.result()
            logging.debug(f'{fn.arg}: value returned: {result}')

    ex = futures.ThreadPoolExecutor(max_workers=2)    
    logging.debug('main: starting')
    f = ex.submit(task, 5)
    # f.arg = 5 # <~ wtf is this line?
    f.add_done_callback(done)
    result = f.result()
    logging.debug(f'result: {result}')

if __name__ == "__main__":
    futures_future_callback()