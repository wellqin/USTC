import sys, signal
sys.path.append('.')
from pkg.breaker import addBreaker
import os, time, threading

def signal_handler(num, stack):
    print('Received signal {} in {}'.format(
        num, threading.currentThread().name
    ))

def wait_for_signal():
    print('Waiting for signal in', threading.currentThread().name)
    pass

@addBreaker
def signal_threads():
    def signal_handler(num, stack):
        print('Received signal {} in {}'.format(
            num, threading.currentThread().name
        ))
    signal.signal(signal.SIGUSR1, signal_handler)
    
    def wait_for_signal():
        print('Waiting for signal in',
                threading.currentThread().name)
        signal.pause()
        print('Done waiting')
    # Start a thread that will not receive the signal.
    receiver = threading.Thread(
        target=wait_for_signal,
        name='receiver',
    )
    receiver.start()
    time.sleep(0.1)

    def send_signal():
        print('Sending signal in', threading.currentThread().name)
        os.kill(os.getpid(), signal.SIGUSR1)

    sender = threading.Thread(target=send_signal, name='sender')
    sender.start()
    sender.join()

    # Wait for the thread to see the signal (not going to happen!).
    print('Waiting for', receiver.name)
    signal.alarm(2)
    receiver.join()

if __name__ == "__main__":
    """
    Mixing signals and threads rarely works well 
    because only the main thread of a process will receive signals. 
    The following example sets up a signal handler, 
    waits for the signal in one thread, and sends the signal from another thread.
    """
    signal_threads()
    ## isn't this wasting time?
    ## yeah.. screw it P597/1454, 20200827 @ZL