import multiprocessing
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def do_calculation(data):
    return data * 2
def start_process():
    logging.debug(f'Starting {multiprocessing.current_process().name}')

if __name__ == '__main__':
    inputs = list(range(10))
    logging.debug(f'Input : {inputs}')
    builtin_outputs = list(map(do_calculation, inputs))
    logging.debug(f'Built-in: {builtin_outputs}')
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
        maxtasksperchild=2, # ! using this argument to tell the pool to restart a worker process after it has finished a few tasks
    )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close() # No more tasks
    pool.join() # Wrap up current tasks.
    logging.debug(f'Pool : {pool_outputs}')