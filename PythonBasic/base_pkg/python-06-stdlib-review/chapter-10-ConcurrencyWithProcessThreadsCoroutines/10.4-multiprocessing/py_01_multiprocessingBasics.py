"""

+----------------------+------------------------+---------------------+
| diff                 | threading              | multiprocessing     |
+======================+========================+=====================+
| args serialization   | NO                     | YES                 |
+----------------------+------------------------+---------------------+
| extra protection for | NO                     | YES                 |
| __main__             |                        |                     |
+----------------------+------------------------+---------------------+
| main thread/process  | sub threads NOT        | sub processes Does  |
| vs                   | block main thread      | block main process  |
| sub threads/processes|                        |                     |
+----------------------+------------------------+---------------------+


"""

import multiprocessing

# @addBreaker
def worker():
    """worker function"""
    print('Worker')

def worker_simpleargs(num):
    """thread worker function"""
    print('Worker:', num)

if __name__ == "__main__":
    ### ! AttributeError: Can't pickle local object 'addBreaker.<locals>.inner'
    ### ! it seems multiprocessing NOT welcome UD decorater?
    ### ! NOPE. Unlike `threading`, the arguments must be serialized using pickle to be passed to a `multiprocessing` Process.
    # print('{:-<50}'.format('-'))
    print('%s' % '-' * 50)
    # jobs = []
    for _ in range(5):
        p = multiprocessing.Process(target=worker)
        # jobs.append(p)
        p.start()
    pass

    ### simple args
    print('%s' % '-' * 50)
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker_simpleargs, args=(i,))
        jobs.append(p)
        p.start()