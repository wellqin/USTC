import atexit
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def all_done():
    logger.debug('all_done()')


logger.debug('Registering')
atexit.register(all_done)
logger.debug('Registered')