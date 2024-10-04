import getpass
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')
u = getpass.getuser()
logging.debug(f'{u}')
