import multiprocessing, logging, sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s, %(funcName)s, %(message)s',
)

def worker():
    logging.debug(f'Doing some work')
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
    pass