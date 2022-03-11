import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')


def sys_stderr():
    logging.debug('STATUS: Reading from stdin, {}'.format(sys.stderr))
    data = 'hello world'
    logging.debug('STATUS: Writing data to stdout, {}'.format(sys.stdout))

    sys.stdout.write(data)
    sys.stdout.flush()

    logging.debug('STATUS: Done, {}'.format(sys.stderr))

def sys_stdout_flush():
    import time
    for i in range(5):
        time.sleep(1)
        # sys.stdout.flush()
        print(i, end=' ')

if __name__ == "__main__":
    sys_stdout_flush()