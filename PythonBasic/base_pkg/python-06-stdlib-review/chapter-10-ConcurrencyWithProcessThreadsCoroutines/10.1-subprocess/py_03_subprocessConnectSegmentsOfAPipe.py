import sys, subprocess
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def subprocess_pipes():
    cat = subprocess.Popen(
        ['cat', 'index.rst'],
        stdout=subprocess.PIPE,
    )
    grep = subprocess.Popen(
        ['grep', '.. literalinclude::'],
        stdin=cat.stdout,
        stdout=subprocess.PIPE,
    )
    cut = subprocess.Popen(
        ['cut', '-f', '3', '-d:'],
        stdin=grep.stdout,
        stdout=subprocess.PIPE,
    )
    end_of_pipe = cut.stdout
    print('Included files:')
    for line in end_of_pipe:
        print(line.decode('utf-8').strip())
    pass

if __name__ == "__main__":
    """
    Multiple commands can be connected into a `pipeline`, 
    similar to the way the Unix shell works, 
    by creating separate Popen instances and chaining their inputs and outputs together.
    
    The stdout attribute of one Popen instance 
    is used as the stdin argument for the next instance in the `pipeline`, 
    
    instead of the constant PIPE. 
    The output is read from the stdout handle for the final command in the `pipeline`
    """
    subprocess_pipes()