import sys, subprocess
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def subprocess_repeater():
    sys.stderr.write('repeater.py: starting\n')
    sys.stderr.flush()
    while True:
        next_line = sys.stdin.readline()
        sys.stderr.flush()
        if not next_line:
            break
        sys.stdout.write(next_line)
        sys.stdout.flush()
    sys.stderr.write('repeater.py: exiting\n')
    sys.stderr.flush()
    pass

@addBreaker
def subprocess_interaction():
    import io
    print('One line at a time:')
    proc = subprocess.Popen(
        'python3 repeater.py',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    stdin = io.TextIOWrapper(
        proc.stdin,
        encoding='utf8',
        line_buffer=True, # send data on newline
    )
    stdout = io.TextIOWrapper(
        proc.stdout,
        encoding='utf8',
    )
    for i in range(5):
        line = '{}\n'.format(i)
        stdin.write(line)
        output = stdout.readline()
        print(output.rstrip())
    remainder = proc.communicate()[0].decode('utf8')
    print(remainder)
    print()
    print('All output at once:')
    proc = subprocess.Popen(
        'python3 repeater.py',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    stdin = io.TextIOWrapper(
        proc.stdin,
        encoding='utf8',
    )
    for i in range(5):
        line = '{}\n'.format(i)
        stdin.write(line)
    stdin.flush()
    output = proc.communicate()[0].decode('utf8')
    print(output)
    pass


if __name__ == "__main__":
    """
    All of the previous examples assume a limited amount of interaction.

    The communicate() method reads all of the output 
    and waits for the child process to exit before returning. 

    It is also possible to write to and read 
    from the individual pipe handles used by the Popen instance incrementally, as the program runs. 
    
    A simple echo program that reads from standard input 
    and writes to standard output illustrates this technique
    """
    subprocess_repeater()
    ### uses the `stdin` and `stdout` file handles owned by the Popen instance in different ways.
    subprocess_interaction()