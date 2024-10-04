import trace
from trace_example.recurse import recurse

tracer = trace.Trace(count=False, trace=True)
tracer.run('recurse(2)')

# or
print()
tracer.runfunc(recurse, 2)