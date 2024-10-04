import socket, logging
from urllib.parse import urlparse
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def socket_getservbyname():
    URLS = [
        'http://www.python.org',
        'https://www.mybank.com',
        'ftp://prep.ai.mit.edu',
        'gopher://gopher.micro.umn.edu',
        'smtp://mail.example.com',
        'imap://mail.example.com',
        'imaps://mail.example.com',
        'pop3://pop.example.com',
        'pop3s://pop.example.com',
    ]
    for url in URLS:
        parsed_url = urlparse(url)
        """
        in addition to an IP address, each socket address includes an integer `port number`.
        
        many applications can run on the same host, listening on a single IP address,
        ! but only one socket at a time can use a port at that address.

        the combination of IP address, protocol, and `port number` uniquely identifies a communication channel 
        and ensures that messages sent throu a socket arrive at the correct destination.

        some of the port numbers are pre-allocated for a specific protocol.
        """
        port = socket.getservbyname(parsed_url.scheme)
        logging.debug('{:>6} : {}'.format(parsed_url.scheme, port))

def socket_getservbyport():
    for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
        url = '{}://example.com/'.format(socket.getservbyport(port))
        logging.debug(f'{url}')

def socket_getprotobyname():
    def get_constants(prefix):
        """
        creates a dictionary mapping socket module constants to their names
        """
        return {
            getattr(socket, n): n
            for n in dir(socket)
            if n.startswith(prefix)
        }
    
    protocols = get_constants('IPPROTO_')

    for name in ['icmp', 'udp', 'tcp']:
        proto_num = socket.getprotobyname(name)
        const_name = protocols[proto_num]
        logging.debug('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(name, proto_num, const_name, getattr(socket, const_name)))

if __name__ == "__main__":
    # socket_getservbyname()
    # socket_getservbyport()
    socket_getprotobyname()