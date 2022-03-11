import sys, subprocess
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def subprocess_os_system():
    p = subprocess.run('dir', shell=True)
    # returncode means exit code 0.
    print('returncode:', p.returncode)
    pass

@addBreaker
def subprocess_run_check():
    try:
        subprocess.run(['false'], check=True)
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)

@addBreaker
def subprocess_run_ouput():
    completed = subprocess.run(
    'dir', 
    shell=True,
    stdout=subprocess.PIPE,
    )
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout:\n{}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'))
    )

@addBreaker
def subprocess_run_output_error():
    try:
        # The message to standard error is printed to the console, 
        # but the message to standard output is hidden.
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('returncode:', completed.returncode)
        print('Have {} bytes in stdout: {!r}'.format(
            len(completed.stdout),
            completed.stdout.decode('utf-8'))
        )
    pass

@addBreaker
def subprocess_run_output_error_trap():
    try:
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('returncode:', completed.returncode)
        print('Have {} bytes in stdout: {!r}'.format(
            len(completed.stdout),
            completed.stdout.decode('utf-8'))
        )
        print('Have {} bytes in stderr: {!r}'.format(
            len(completed.stderr),
            completed.stderr.decode('utf-8'))
        )
    pass

@addBreaker
def subprocess_check_output_error_trap_output():
    try:
        output = subprocess.check_output(
            'echo to stdout; echo to stderr 1>&2',
            shell=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('Have {} bytes in output: {!r}'.format(
            len(output),
            output.decode('utf-8'))
        )
    pass

@addBreaker
def subprocess_run_output_error_suppress():
    try:
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('returncode:', completed.returncode)
        print('stdout is {!r}'.format(completed.stdout))
        print('stderr is {!r}'.format(completed.stderr))
    pass

if __name__ == "__main__":
    ### CLI + subprocess works greate
    ### run(), check_all(), call() could be equivalent to each other by passing `check=True`
    # subprocess_os_system()
    ### error handling
    # subprocess_run_check() # works on unix-like sys only
    ### capture output
    # subprocess_run_ouput()
    ### runs a series of commands in a subshell
    # subprocess_run_output_error()
    ### To prevent error messages from commands run through run() from being written to the
    ### console, set the stderr parameter to the constant PIPE.
    subprocess_run_output_error_trap()
    ### To capture error messages when using check_output(), set stderr to STDOUT, 
    ### and the messages will be merged with the rest of the output from the command
    subprocess_check_output_error_trap_output()
    ### For cases where the output should not be shown or captured, use DEVNULL to suppress an
    ### output stream. The next example suppresses both the standard output and error streams.
    subprocess_run_output_error_suppress()