import sys, threading, time, logging, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def threading_enumerate():
    def worker():
        """thread worker function"""
        pause = random.randint(1, 5) / 10
        logging.debug('sleeping %0.2f', pause)
        time.sleep(pause)
        logging.debug('ending')

    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    for _ in range(3):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
    
    main_thread = threading.main_thread()

    for t in threading.enumerate():
        if t is main_thread:
            continue
        logging.debug('joining %s', t.getName())
        t.join()
    pass

if __name__ == "__main__":
    threading_enumerate()