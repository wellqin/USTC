import sys, subprocess
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def subprocess_signal_parent():
    import os
    import signal
    import subprocess
    import time
    import sys
    proc = subprocess.Popen(['python3', 'signal_child.py'])
    print('PARENT : Pausing before sending signal...')
    sys.stdout.flush()
    time.sleep(1)
    print('PARENT : Signaling child')
    sys.stdout.flush()
    os.kill(proc.pid, signal.SIGUSR1)
    pass

@addBreaker
def subprocess_signal_parent_shell():
    import os
    import signal
    import subprocess
    import tempfile
    import time
    import sys
    script = '''#!/bin/sh
    echo "Shell script in process $$"
    set -x
    python3 signal_child.py
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()
    proc = subprocess.Popen(['sh', script_file.name])
    print('PARENT : Pausing before signaling {}...'.format(
    proc.pid))
    sys.stdout.flush()
    time.sleep(1)
    print('PARENT : Signaling child {}'.format(proc.pid))
    sys.stdout.flush()
    os.kill(proc.pid, signal.SIGUSR1)
    time.sleep(3)
    pass

@addBreaker
def subprocess_signal_setpgrp():
    import os
    import signal
    import tempfile
    import time
    import sys

    def show_setting_prgrp():
        print('Calling os.setpgrp() from {}'.format(os.getpid()))
        os.setpgrp()
        print('Process group is now {}'.format(os.getpid(), os.getpgrp()))
        sys.stdout.flush()

    script = '''#!/bin/sh
    echo "Shell script in process $$"
    set -x
    python3 signal_child.py
    '''
    script_file = tempfile.NamedTemporaryFile('wt')
    script_file.write(script)
    script_file.flush()

    proc = subprocess.Popen(
        ['sh', script_file.name],
        preexec_fn=show_setting_prgrp,
    )
    print('PARENT : Pausing before signaling {}...'.format(proc.pid))
    sys.stdout.flush()
    time.sleep(1)
    print('PARENT : Signaling process group {}'.format(proc.pid))
    sys.stdout.flush()
    os.killpg(proc.pid, signal.SIGUSR1)
    time.sleep(3)
    pass


if __name__ == "__main__":
    """
    Since each `Popen` instance provides a `pid` attribute with the process ID of the child process, 
    it is possible to do something similar with subprocess.
    """
    subprocess_signal_parent()  # works on unix-like os