from urllib.parse import urlparse, urlunparse
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def urllib_parse_geturl():
    original = 'http://netloc/path;param?query=arg#frag'
    parsed   = urlparse(original)
    logging.debug(f'ORIG    : {original}')
    """
    geturl() ONLY works on the object returned by `urlparse()` or `urlsplit()`
    
    ? but i have no f*cking idea how can u reassemble the parts of a split URL into a single string by using `geturl()` tho?
    * A: ?
    
    """
    logging.debug(f'PARSED  : {parsed.geturl()}')


def urllib_parse_urlunparse():
    original = 'http://netloc/path;param?query=arg#frag'
    parsed   = urlparse(original)
    """
    this line is just for science.
    intends to show that `urlunparse()` works on a normal tuple as well.
    """
    t        = parsed[:]
    logging.debug(f'ORIG    : {original}')
    logging.debug(f'PARSED  : {type(parsed)}, {parsed}')
    logging.debug(f'TUPLE   : {type(t)}, {t}')
    logging.debug(f'NEW     : {urlunparse(t)}')

def urllib_parse_urlunparseextra():
    original = 'http://netloc/path;?#'  # ! this line is different
    parsed   = urlparse(original)
    t        = parsed[:]
    logging.debug(f'ORIG    : {original}')
    logging.debug(f'PARSE   : {type(parsed)}, {parsed}')
    logging.debug(f'TUPLE   : {type(t)}, {t}')
    logging.debug(f'NEW     : {urlunparse(t)}')
    ...

if __name__ == "__main__":
    urllib_parse_geturl()
    print()
    urllib_parse_urlunparse()
    print()
    urllib_parse_urlunparseextra()