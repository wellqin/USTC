import sched
import time

# creates a scheduler
# scheduler = sched.scheduler()   # <~ this works too ..
scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name, start):
    now     = time.time()
    elapsed = int(now - start)
    print('EVENT: {} elapsed={} name={}'.format(time.ctime(now), elapsed, name))

start = time.time()
print('START:', time.ctime(start))
"""
wait a second

isn't the concept of `sched` similar with asyncio or threading or multiprocessing?
"""
scheduler.enter(2, 1, print_event, ('first', start))
scheduler.enter(3, 1, print_event, ('second', start))
scheduler.run()