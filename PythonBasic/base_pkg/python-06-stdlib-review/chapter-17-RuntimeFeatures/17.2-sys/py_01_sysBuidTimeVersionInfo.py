import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

for i in [
    'version',
    'version_info',
    'hexversion',
    'api_version',
    'platform', # os platform used to build the interpreter
    'implementation', # detect the current implementation for libraries that need to work around any differences in interpreters.
]:
    logging.debug('sys.{:12} = {}'.format(i, getattr(sys, i)))


logging.debug(f'{"-" * 20}')
# this value is set during start-up, and cannot be changed during a session
logging.debug('Default encoding     :{}'.format(sys.getdefaultencoding()))
# the internal encoding default and the file system encoding may be different for some operating systems
# so there is a separate way to retrieve the file system setting.
logging.debug('File System encoding :{}'.format(sys.getfilesystemencoding()))
# rather than relying on the global default encoding,
# most Unicode experts recommend making an application explicitly Unicode-aware.