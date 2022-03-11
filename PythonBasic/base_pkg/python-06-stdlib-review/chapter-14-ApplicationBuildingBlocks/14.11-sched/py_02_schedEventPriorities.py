import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
    print('EVENT:', time.ctime(time.time()), name)

now = time.time()
print('START:', time.ctime(now))
"""
! This example needs to ensure that the events are scheduled for the exact same time, so
the enterabs() method is used instead of enter(). 

The first argument to enterabs() is the
time to run the event, instead of the amount of time to delay its start.
"""
scheduler.enterabs(now + 2, 2, print_event, ('first',))
scheduler.enterabs(now + 2, 1, print_event, ('second',))

scheduler.run()