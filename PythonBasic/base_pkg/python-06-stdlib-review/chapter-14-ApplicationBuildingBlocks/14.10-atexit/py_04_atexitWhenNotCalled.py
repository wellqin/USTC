import atexit
import sys

def all_done():
    print('all_done()')

print('Registering')
atexit.register(all_done)
print('Registered')

print('Exiting...')
"""
To ensure that the callbacks are run, 
allow the program to terminate by running out of
statements to execute or by calling `sys.exit()`
"""
sys.exit()