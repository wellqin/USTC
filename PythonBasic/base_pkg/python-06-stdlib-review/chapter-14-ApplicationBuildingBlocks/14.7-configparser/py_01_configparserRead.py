from configparser import ConfigParser
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

parser = ConfigParser()
parser.read(r"chapter-14-ApplicationBuildingBlocks\14.7-configparser\simple.ini")
logging.debug(parser.get('bug_tracker', 'url'))

