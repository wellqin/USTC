import sched, time
import threading

scheduler = sched.scheduler(time.time, time.sleep)

# setup a global to be modified by the threads
counter = 0

def increment_counter(name):
    global counter
    print('EVENT:', time.ctime(time.time()), name)
    counter += 1
    print('NOW:', counter)

print('START:', time.ctime(time.time()))
e1 = scheduler.enter(2, 1, increment_counter, ('E1',))
e2 = scheduler.enter(3, 1, increment_counter, ('E2',))

# start a thread to run the events
t = threading.Thread(target=scheduler.run)
t.start()

# back in the main thread, cancel the first scheduled event
scheduler.cancel(e1)
t.join()

print('FINAL:', counter)