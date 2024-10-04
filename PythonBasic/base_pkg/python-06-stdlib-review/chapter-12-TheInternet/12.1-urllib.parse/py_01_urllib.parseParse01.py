"""

? urlib in Python 2.x vs Python 3.x?
link: https://blog.csdn.net/old__tree/article/details/79872490

python2中有urllib、urllib2、urlparse，但在python3中这些全部都被整合到了urllib中。
urllib和urllib2中的内容整合进了urllib.request模块中，urlparse整合进了urllib.parse中。
python3中urllib中还包括response、error和robotparse这些子模块。

? why not work?
link: https://stackoverflow.com/questions/41501638/attributeerror-module-urllib-has-no-attribute-parse

The urllib package serves as a namespace only. 
There are other modules under urllib like request and parse.

For optimization importing urllib doesn't import other modules under it. 
Because doing so would consume processor cycles and memory, but people may not need those other modules.

Individual modules under urllib must be imported separately depending on the needs.

"""

from urllib.parse import urlparse, urlsplit, urldefrag
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def urllib_parse_urlparse():
    url    = 'http://netloc/path;param?query=arg#frag'
    # parsed = urllib.parse.urlparse(url) # ? this one f*cked, but why? namespace issue?
    """
    * i recall os.path vs pathlib
    * i recall asyncio.getaddrinfo() vs asyncio.getnameinfo()
    * i recall socket.socket(), selectors, select, 
    * i recall ipaddress.ip_address(), ipaddress.ip_network(), ipaddress.ip_interface()
    * i f*ck know some shit?
    """
    parsed = urlparse(url)
    logging.debug(f'parsed: {parsed}')

def urllib_parse_urlparseattrs():
    url    = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
    parsed = urlparse(url)
    logging.debug('scheme   : {}'.format(parsed.scheme))
    logging.debug('netloc   : {}'.format(parsed.netloc))
    logging.debug('path     : {}'.format(parsed.path))
    logging.debug('params   : {}'.format(parsed.params))
    logging.debug('query    : {}'.format(parsed.query))
    logging.debug('fragment : {}'.format(parsed.fragment))
    logging.debug('username : {}'.format(parsed.username))
    logging.debug('password : {}'.format(parsed.password))
    logging.debug('hostname : {}'.format(parsed.hostname))
    logging.debug('port     : {}'.format(parsed.port))

def urllib_parse_urlsplit():
    """
    urlparse() vs urlsplit()
    an alternative
    
    +---------------+---------------------+---------------------+
    | items         | urlparse()          | urlsplit()          |
    +===============+=====================+=====================+
    | return value  | 6-namedtuple obj    | 5-namedtuple obj    |
    +---------------+---------------------+---------------------+
    | split params  | Yes                 | No                  |
    | from URL?     |                     |                     |
    +---------------+---------------------+---------------------+
    | when to use?  | normal              | RFC 2396            |
    +---------------+---------------------+---------------------+

    ? wtf is RFC 2396?
    * A: we need some means to identify a resource. Uniform Resource Identifier(URI)
    * this specification of URI syntax and semantics is derived from concepts introduced by the World Wide Web global information initiative,
    * whose use of such objects dates from 1990 and is described in "Universal Resource Identifiers in WWW" [RFC1630].
    * the specifiication of URI is designed to meet the recommendation laid out in "Functional Recommendations for Internet Resource Locators" [RFC1736]
    * and "Functional Requirements for Uniform Resource Names" [RFC1737]
        - RFC 1738: Uniform Resource Locator (URL) syntax
        - RFC 1808: Relative URLs
        - RFC 2396: Uniform Resource Identifier (URI) generic syntax
        - RFC 3986: Uniform Resource Identifier (URI) syntax

    link: https://tools.ietf.org/html/rfc2396.html
    """
    url    = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
    parsed = urlsplit(url)
    logging.debug('scheme   : {}'.format(parsed.scheme))
    logging.debug('netloc   : {}'.format(parsed.netloc))
    logging.debug('path     : {}'.format(parsed.path))
    # logging.debug('params   : {}'.format(parsed.params))
    logging.debug('query    : {}'.format(parsed.query))
    logging.debug('fragment : {}'.format(parsed.fragment))
    logging.debug('username : {}'.format(parsed.username))
    logging.debug('password : {}'.format(parsed.password))
    logging.debug('hostname : {}'.format(parsed.hostname))
    logging.debug('port     : {}'.format(parsed.port))

def urllib_parse_urldefrag():
    """
    ? wtf is urldefrag()?
    * it simply strip the fragment identifier from a URL,
    * such as when finding a base page name from a URL
    """
    original = 'http://netloc/path;param?query=arg#frag'
    d        = urldefrag(original)
    logging.debug(f'original    : {original}')
    logging.debug(f'url         : {d.url}')
    logging.debug(f'fragment    : {d.fragment}')
    ...

if __name__ == "__main__":
    urllib_parse_urlparse()
    print()
    urllib_parse_urlparseattrs()
    print()
    urllib_parse_urlsplit()
    print()
    urllib_parse_urldefrag()