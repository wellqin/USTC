import trace
import pathlib
from trace_example.recurse import recurse

tracer = trace.Trace(count=True, trace=False)
tracer.runfunc(recurse, 2)

results = tracer.results()
results.write_results(coverdir=pathlib.Path(__file__).parent / 'coverdir2')