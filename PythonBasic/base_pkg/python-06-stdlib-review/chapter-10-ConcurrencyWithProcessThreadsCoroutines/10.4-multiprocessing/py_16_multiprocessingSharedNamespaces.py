import multiprocessing, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
)

def producer(ns, event):
    ns.value = 'This is the value'
    event.set()

def consumer(ns, event):
    try:
        logging.debug(f'Before event: {ns.value}')
    except Exception as err:
        logging.debug(f'Before event, error: {err}')
    event.wait()
    logging.debug(f'After event: {ns.value}', )

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    event = multiprocessing.Event()
    p = multiprocessing.Process(
        target=producer,
        args=(namespace, event),
    )
    c = multiprocessing.Process(
        target=consumer,
        args=(namespace, event),
    )

    c.start()
    p.start()

    c.join()
    p.join()