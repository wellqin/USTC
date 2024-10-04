import sys, signal
sys.path.append('.')
from pkg.breaker import addBreaker
import os, time

def receive_signal(signum, stack):
    print('Received:', signum)

@addBreaker
def signal_signal():
    # register signal handlers
    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGINT, receive_signal)
    # print the process ID so it can be used with 'kill'
    # to send this program signals.
    print('My PID is:', os.getpid())
    while True:
        print('Waiting...')
        time.sleep(3)
    pass

if __name__ == "__main__":
    """
    SIGALRM is not supported on Windows. https://docs.python.org/2/library/signal.html 
    On Windows, signal() can only be called with 
    SIGABRT, SIGFPE, SIGILL, SIGINT, SIGSEGV, or SIGTERM. 
    
    A ValueError will be raised in any other case
    """
    ### send signals to the running program using os.kill()
    signal_signal()