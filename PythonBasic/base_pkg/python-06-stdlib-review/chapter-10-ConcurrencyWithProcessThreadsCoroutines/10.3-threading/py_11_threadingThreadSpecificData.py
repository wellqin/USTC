import sys, threading, random, logging
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def threading_local():
    def show_value(data):
        try:
            val = data.value
        except AttributeError:
            logging.debug('No value yet')
        else:
            logging.debug('value=%s', val)

    def worker(data):
        show_value(data)
        data.value = random.randint(1, 100)
        show_value(data)
        
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    local_data = threading.local()
    show_value(local_data)
    local_data.value = 1000
    show_value(local_data)

    for _ in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()
    pass

@addBreaker
def threading_local_defaults():
    def show_value(data):
        try:
            val = data.value
        except AttributeError:
            logging.debug('No value yet')
        else:
            logging.debug('value=%s', val)

    def worker(data):
        show_value(data)
        data.value = random.randint(1, 100)
        show_value(data)

    class MyLocal(threading.local):
        def __init__(self, value):
            super().__init__()
            logging.debug('Initializing %r', self)
            self.value = value

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

    local_data = MyLocal(1000)
    show_value(local_data)
    for _ in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()
    pass

if __name__ == "__main__":
    """
    while some resources need to be locked so multiple threads can use them,
    others need to be protected so that they are hidden from threads that do not own them.

    the `local()` class creates an object 
    capable of hiding values from view in separate threads.
    
    """
    threading_local()

    """
    To initialize the settings so all threads start with the same value, 
    use a subclass and set the attributes in __init__().
    """
    threading_local_defaults()