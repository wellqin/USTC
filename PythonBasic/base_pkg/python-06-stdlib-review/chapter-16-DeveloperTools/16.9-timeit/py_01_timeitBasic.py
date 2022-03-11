import timeit

# uses setitem
"""
timeit() runs the setup statement one time, 
then calls the main statement count times
"""
t = timeit.Timer('print("main statement")', 'print("setup")')
print('TIMEIT:')
print(t.timeit(2))
print('\nREPEAT:')
print(t.repeat(3, 2))