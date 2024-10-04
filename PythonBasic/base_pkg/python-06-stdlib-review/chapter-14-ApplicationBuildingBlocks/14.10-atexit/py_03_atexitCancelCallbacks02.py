import atexit

def my_cleanup(name):
    print('my_cleanup({})'.format(name))

if False:
    atexit.register(my_cleanup, 'never registered')

"""
unregistering a function that is not registered previously
incurs no errors.

? why?

Because it silently ignores unknown callbacks, 
unregister() can be used even when the
sequence of registrations is not known.
"""
atexit.unregister(my_cleanup)