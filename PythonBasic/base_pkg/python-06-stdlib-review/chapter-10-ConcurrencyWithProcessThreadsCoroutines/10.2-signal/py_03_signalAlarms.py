import sys, signal
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def signal_alarm():
    import time
    def receive_alarm(signum, stack):
        print('Alarm :', time.ctime())
    # call received_alarm in 2 seconds
    signal.signal(signal.SIGALRM, receive_alarm)
    signal.alarm(2)
    print('Before:', time.ctime())
    time.sleep(4)
    print('After :', time.ctime())
    pass

if __name__ == "__main__":
    signal_alarm()