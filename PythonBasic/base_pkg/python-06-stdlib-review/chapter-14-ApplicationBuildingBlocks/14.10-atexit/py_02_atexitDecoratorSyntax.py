import atexit

"""
this atexit.register decorator only works on
non-arguments functions.
"""
@atexit.register
def all_done():
    print('all_done()')

print('starting main program')