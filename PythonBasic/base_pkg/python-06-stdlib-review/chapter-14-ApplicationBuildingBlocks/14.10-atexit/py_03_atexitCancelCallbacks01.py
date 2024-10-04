import atexit

def my_cleanup(name):
    print('my_cleanup({})'.format(name))

atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')
# ! unregister all same functions in one shot, no matter that how many times it has been registered.
atexit.unregister(my_cleanup)