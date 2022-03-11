import atexit
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def my_cleanup(name):
    logger.debug('my_cleanup({})'.format(name))

"""
? Q: why output is reversed order?
* A: This method allows modules to be cleaned up in the reverse order from which they are
* A: imported (and therefore register their atexit functions), which should reduce dependency conflicts.
"""
atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')