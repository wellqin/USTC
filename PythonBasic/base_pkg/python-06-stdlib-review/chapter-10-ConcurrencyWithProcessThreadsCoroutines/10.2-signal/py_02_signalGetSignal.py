import sys, signal
sys.path.append('.')
from pkg.breaker import addBreaker


def alarm_received(n, stack):
    return


@addBreaker
def signal_getsignal():
    signal.signal(signal.SIGALRM, alarm_received)
    signals_to_names = {
        getattr(signal, n): n
        for n in dir(signal)
        if n.startswith('SIG') and '_' not in n
    }
    
    for s, name in sorted(signals_to_names.items()):
        handler = signal.getsignal(s)
        if handler in signal.SIG_DFL:
            handler = 'SIG_DFL'
        elif handler is signal.SIG_IGN:
            handler = 'SIG_IGN'
        print('{:<10} ({:2d})'.format(name, s), handler)
    
    pass


if __name__ == "__main__":
    signal_getsignal()
    ### the funciton used to send signals from within Python is `os.kill()`
    