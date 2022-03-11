import multiprocessing, time, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
)

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)  # ? but wtf is this line? seems a different approach to initialize base class
        self.task_queue   = task_queue
        self.result_queue = result_queue
    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # poison pill means shutdown
                logging.debug(f'{proc_name}: existing')
                self.task_queue.task_done()
                break
            logging.debug(f'{proc_name}: {next_task}')
            # ! "Task" object is callable
            answer = next_task() 
            self.task_queue.task_done()
            self.result_queue.put(answer)
    pass

class Task:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        time.sleep(.1)  # pretend to take time to do the work
        return f'{self.a} * {self.b} = {self.a * self.b}'
    def __str__(self):
        return f'{self.a} * {self.b}'
    pass

if __name__ == "__main__":
    ### establishes communicate queues.
    tasks   = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    ### starts consumers
    num_consumers = multiprocessing.cpu_count() * 2
    logging.debug(f'creating {num_consumers} consumers')
    consumers = [
        Consumer(tasks, results)
        for _ in range(num_consumers)
    ]
    for w in consumers:
        w.start()
    
    ### Enqueues jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))
    ### adds poison pill for each consumer
    for _ in range(num_consumers):
        tasks.put(None)
    ### wait for all of the tasks to finish
    tasks.join()
    ### start printing results
    while num_jobs:
        result = results.get()
        logging.debug(f'Result: {result}')
        num_jobs -=1
    logging.debug(f'cpu cores: {multiprocessing.cpu_count()}')