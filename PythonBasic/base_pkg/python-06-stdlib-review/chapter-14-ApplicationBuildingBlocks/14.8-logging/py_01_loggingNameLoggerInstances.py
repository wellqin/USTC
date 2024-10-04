import logging
logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('this msg comes from module1')
logger2.warning('this msg comes from module2')