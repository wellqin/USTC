"""
! what?
`traceback` works with the call stack to produce error messages.

a "traceback" is a stack trace from the point of an exception handler
down the call chain to the point where the exception was raised.

tracebacks also can be accessed from the current call stack up
from the point of a call (and w/o the context of an error),
which is useful for determining the paths being followed into a function.


! why?
stfu

! how?

traceback: exception and stack traces
|-- support functions
|-- examine the stack
|-- TracebackException
|-- low-level exception APIs
|-- low-level stack APIs

"""