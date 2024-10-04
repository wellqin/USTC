import sys, subprocess
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def subprocess_popen_read():
    print('read:')
    proc = subprocess.Popen(
        ['echo', '"to stdout"'],
        stdout=subprocess.PIPE,
    )
    # ! process.communicate()
    stdout_value = proc.communicate()[0].decode('utf-8')
    print('stdout:', repr(stdout_value))
    pass

@addBreaker
def subprocess_popen_write():
    print('write:')
    proc = subprocess.Popen(
        ['cat', '-'],
        stdin=subprocess.PIPE,
    )
    proc.communicate('stdin: to stdin\n'.encode('utf-8'))
    pass

@addBreaker
def subprocess_popen2():
    print('popen2:')
    proc = subprocess.Popen(
        ['cat', '-'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    msg = 'through stdin to stdout'.encode('utf-8')
    stdout_value = proc.communicate(msg)[0].decode('utf-8')
    print('pass through:', repr(stdout_value))
    pass

@addBreaker
def subprocess_popen3():
    print('popen3:')
    proc = subprocess.Popen(
        'cat -; echo "to stderr" 1>&2',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    msg = 'through stdin to stdout'.encode('utf-8')
    stdout_value, stderr_value = proc.communicate(msg)
    print('pass through :', repr(stdout_value.decode('utf-8')))
    print('stderr       :', repr(stderr_value.decode('utf-8')))
    pass

@addBreaker
def subprocess_popen4():
    print('popen4:')
    proc = subprocess.Popen(
        'cat -; echo "to stderr" 1>&2',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    msg = 'through stdin to stdout\n'.encode('utf-8')
    stdout_value, stderr_value = proc.communicate(msg)
    print('combined output  :', repr(stdout_value.decode('utf-8')))
    print('stderr value     :', repr(stderr_value))
    pass

if __name__ == "__main__":
    """
    The functions `run()`, `call()`, `check_call()`, and `check_output()` 
    are wrappers around the `Popen` class

    Using `Popen` directly gives more control over how the command is run, 
    and how its input and output streams are processed
    """
    ### one-way communication with a process
    # subprocess_popen_read() # works on unix-like os
    ### To set up a pipe to allow the calling program to write data to it, set stdin to `PIPE`.
    subprocess_popen_write()
    ### To set up the Popen instance for reading and writing at the same time, 
    ### use a combination of the previous techniques.
    subprocess_popen2()
    ### It is also possible to watch both of the streams for stdout and stderr
    ### Reading from stderr works the same way as reading from stdout. 
    ### Passing PIPE tells Popen to attach to the channel, 
    ### and communicate() reads all of the data from it before returning
    subprocess_popen3()
    ### To direct the error output from the process to its standard output channel, 
    ### use STDOUT for stderr instead of PIPE
    subprocess_popen4()