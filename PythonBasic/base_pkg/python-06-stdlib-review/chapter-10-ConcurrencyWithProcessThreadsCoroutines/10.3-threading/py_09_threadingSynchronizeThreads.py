"""

+--------+--------------------+------------------------------------------------------------------+
| Lock   | Full Name          | Notation                                                         |
+========+====================+==================================================================+
| Lock   | Normal `Lock`      | cant NOT be acquired more than ONCE, even by the same thread.    |
+--------+--------------------+------------------------------------------------------------------+
| RLock  | "reacquire" `Lock` | in a situation where separate code from the same thread          |
|        |                    | needs to "reacqure" the lock                                     |
+--------+--------------------+------------------------------------------------------------------+


"""



import sys, threading, time, logging
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def threading_condition():
    def consumer(cond):
        """wait for the condition and use the resource"""
        logging.debug('Starting consumer thread')
        with cond:
            cond.wait()
            logging.debug('Resource is available to consumer')

    def producer(cond):
        """set up the resource to be used by the consumer"""
        logging.debug('Starting producer thread')
        with cond:
            logging.debug('Making resource available')
            cond.notifyAll()

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s (%(threadName)-2s) %(message)s',
    )

    condition = threading.Condition()
    c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
    c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
    p  = threading.Thread(name='p', target=producer, args=(condition,))

    c1.start()
    time.sleep(0.2)
    c2.start()
    time.sleep(0.2)
    p.start()
    pass

@addBreaker
def threading_barrier():
    def worker(barrier):
        print(threading.current_thread().name,
            'waiting for barrier with {} others'.format(barrier.n_waiting),
        )
        worker_id = barrier.wait()
        print(threading.current_thread().name, 'after barrier', worker_id)

    NUM_THREADS = 3
    barrier = threading.Barrier(NUM_THREADS)
    
    threads = [
        threading.Thread(
            name='worker-%s' % i,
            target=worker,
            args=(barrier,),
        )
        for i in range(NUM_THREADS)
    ]

    for t in threads:
        print(t.name, 'starting')
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()

    pass

@addBreaker
def threading_barrier_abort():
    def worker(barrier):
        print(threading.current_thread().name, 'waiting for barrier with {} others'.format(barrier.n_waiting))
        try:
            worker_id = barrier.wait()
        except threading.BrokenBarrierError:
            print(threading.current_thread().name, 'aborting')
        else:
            print(threading.current_thread().name, 'after barrier', worker_id)
    
    NUM_THREADS = 3

    barrier = threading.Barrier(NUM_THREADS + 1)
    threads = [
        threading.Thread(
        name='worker-%s' % i,
        target=worker,
        args=(barrier,),
        )
        for i in range(NUM_THREADS)
    ]

    for t in threads:
        print(t.name, 'starting')
        t.start()
        time.sleep(0.1)
        barrier.abort()
        
    for t in threads:
        t.join()
    pass



if __name__ == "__main__":
    """
    In addition to using Events, another way of synchronizing threads is by using a Condition
    object. 

    Because the Condition uses a Lock, it can be tied to a shared resource, allowing
    multiple threads to wait for the resource to be updated. 

    In the next example, the consumer()
    threads wait for the Condition to be set before continuing. 

    The producer() thread is
    responsible for setting the condition and notifying the other threads that they can
    continue.
    
    """
    threading_condition()

    ### Barriers are another thread synchronization mechanism.
    ### A Barrier establishes a control point, and all participating threads then 
    ### block until all of the participating “parties” have reached that point.
    ### With this approach, threads can start up separately and then pause until they are all ready to proceed.
    threading_barrier()
    ### barrier abort()
    threading_barrier_abort()