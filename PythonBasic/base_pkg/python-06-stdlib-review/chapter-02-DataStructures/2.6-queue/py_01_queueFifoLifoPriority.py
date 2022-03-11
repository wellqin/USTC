import queue, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def queue_fifo():
    q = queue.Queue()
    for i in range(5):
        q.put(i)
    while not q.empty():
        print(q.get(), end=' ')
    print()

@addBreaker
def queue_lifo():
    q = queue.LifoQueue()
    for i in range(5):
        q.put(i)
    while not q.empty():
        print(q.get(), end=' ')
    print()

@addBreaker
def queue_priority():
    import functools, threading
    # a class holds priority and description of a job
    @functools.total_ordering
    class Job:
        def __init__(self, priority, description):
            self.priority    = priority
            self.description = description
            print('New job:', description)
        def __eq__(self, other):
            try:
                return self.priority == other.priority
            except AttributeError:
                return NotImplemented
        def __lt__(self, other):
            try:
                return self.priority < other.priority
            except AttributeError:
                return NotImplemented
    # create a PriorityQueue
    q = queue.PriorityQueue()
    q.put(Job(3, 'Mid-level job'))
    q.put(Job(10, 'Low-level job'))
    q.put(Job(1, 'Important job'))
    # do jobs inside of a PriorityQueue
    def process_job(q: queue):
        while True:
            next_job = q.get()
            print('Processing job:', next_job.description)
            q.task_done()
    # threading
    workers = [
        threading.Thread(target=process_job, args=(q,)),
        threading.Thread(target=process_job, args=(q,)),
    ]
    # start jobs
    for worker in workers:
        worker.setDaemon(True)
        worker.start()
    q.join()

def main():
    # basic fifo queue
    queue_fifo()
    # ? lifo queue. isn't if a stack?
    queue_lifo()
    # priority queue
    queue_priority()

if __name__ == "__main__":
    main()
