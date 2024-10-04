"""
poorly designed library code may write directly to `sys.stdout` or `sys.stderr`,
w/o providing arguments to configure different output destinations

! interesting. I had encountered a similar problem once. SoX :^)
`redirect_stdout()` and `redirect_stderr()` context managers can be used to 
capture output from these kinds of functions, 
for which the source cannot be changed to accept a new output argument

"""


import contextlib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from typing import Any
import io

def misbehaving_function(a: Any):
    sys.stdout.write('(stdout) A: {!r}\n'.format(a))
    sys.stderr.write('(stderr) A: {!r}\n'.format(a))

@addBreaker
def contextlib_redirect():
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
        misbehaving_function(5)
    print(capture.getvalue())

if __name__ == "__main__":
    contextlib_redirect()