import pprint, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from py_pprint_data import data

@addBreaker
def print_vs_pprint():
    print('PRINT:')
    print(data)
    print('\nPPRINT:')
    pprint.pprint(data)

@addBreaker
def pprint_pformat():
    import logging
    logging.basicConfig(
        level = logging.DEBUG,
        format= '%(levelname)-8s %(message)s',
    )
    logging.debug('Logging pformatted data')
    formatted = pprint.pformat(data)
    for line in formatted.splitlines():
        logging.debug(line.rstrip())

if __name__ == "__main__":
    # use by default
    print_vs_pprint()
    # formatting
    pprint_pformat()