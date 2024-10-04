import sys
# import logging
# logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

print('initial limit : {}'.format(sys.getrecursionlimit()))
sys.setrecursionlimit(10)
print('Modified limit: {}'.format(sys.getrecursionlimit()))

def generate_recursion_error(i):
    print('generate_recursino_error({})'.format(i))
    generate_recursion_error(i + 1)

try:
    generate_recursion_error(1)
except RuntimeError as err:
    print('Caught exception: {}'.format(err))