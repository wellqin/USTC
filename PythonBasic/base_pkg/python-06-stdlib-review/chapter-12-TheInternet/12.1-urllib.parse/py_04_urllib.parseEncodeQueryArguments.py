from urllib.parse import urlencode, parse_qs, parse_qsl
from urllib.parse import quote, quote_plus
from urllib.parse import unquote, unquote_plus
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def urllib_parse_urlencode():
    query_args = {
        'q': 'query string',
        'foo': 'bar',
    }
    encoded_args = urlencode(query_args)
    logging.debug(f'Encoce  : {encoded_args}')

def urllib_parse_urlencode_doseq():
    query_args = {
        'foo': ['foo1', 'foo2']
    }
    logging.debug(f'Single      : {urlencode(query_args)}')
    logging.debug(f'Sequence    : {urlencode(query_args, doseq=True)}')

def urllib_parse_parse_qs():
    """
    pairs, pairs everywhere

    +---------------+-------------------+-------------------+
    | items         | parse_qs()        | parse_qsl()       |
    +===============+===================+===================+
    | return values | dict              | list of tuples    |
    +---------------+-------------------+-------------------+

    """
    encoded = 'foo=foo1&foo=foo2'
    logging.debug(f'parse_qs    : {parse_qs(encoded)}')
    logging.debug(f'parse_qsl   : {parse_qsl(encoded)}')

def urllib_parse_quote():
    url = 'http://localhost:8080/~hellmann/'
    logging.debug('urlencode()  :   {}'.format(urlencode({'url': url})))
    logging.debug(f'quote()      :   {quote(url)}')
    logging.debug(f'quote_plus() :   {quote_plus(url)}')

def urllib_parse_unquote():
    """
    pairs everywhere, wtf
    """
    q1 = r'http%3A//localhost%3A8080/%7Ehellmann/'
    q2 = r'http%3A%2F%2Flocalhost%3A8080%2F%7Ehellmann%2F'
    logging.debug('{}'.format(unquote(q1)))
    logging.debug('{}'.format(unquote_plus(q2)))
    ...
    

if __name__ == "__main__":
    urllib_parse_urlencode()
    print()
    urllib_parse_urlencode_doseq()
    print()
    urllib_parse_parse_qs()
    print()
    urllib_parse_quote()
    print()
    urllib_parse_unquote()