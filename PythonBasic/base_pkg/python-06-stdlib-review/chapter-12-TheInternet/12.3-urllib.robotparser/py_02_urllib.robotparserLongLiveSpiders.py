from urllib import robotparser
import time

AGENT_NAME = 'PyMOTW'
parser = robotparser.RobotFileParser()
# use the local copy
"""
an application that takes a long time to process the resources
it downloads or that is throttled to pause btwn downloads should check for new `robots.txt` files periodically 
based on the age of the content it has already downloaded.

the age is NOT managed automatically 
but convience methods are available to facilitate its tracking.

"""
parser.set_url('file:robots.txt')
parser.read()
parser.modified()

PATHS = [
    '/',
    '/PyMOTW',
    '/admin',
    '/downloads/PyMOTW-1.92.tar.gz',
]

for path in PATHS:
    age = int(time.time() - parser.mtime())
    print('age:', age, end=' ')
    if age > 1:
        print('rereading robots.txt')
        parser.read()
        parser.modified()
    else:
        print()
    print('{!r:6} : {}'.format(parser.can_fetch(AGENT_NAME, path), path))
    # simulates a delay in processing
    time.sleep(1)
    print()
