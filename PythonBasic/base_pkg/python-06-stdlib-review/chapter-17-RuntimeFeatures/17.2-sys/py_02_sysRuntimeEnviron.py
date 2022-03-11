import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

logging.debug('Arguments: {!r}'.format(sys.argv))