import socket
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def socket_gethostname():
    # finds the official name of the current host
    logging.debug(socket.gethostname())

def socket_gethostbyname():
    HOSTS = [
        'apu',
        'pymotw.com',
        'www.python.org',
        'nosuchname',
    ]

    for host in HOSTS:
        try:
            logging.debug('{:14} : {}'.format(host, socket.gethostbyname(host)))
        except socket.error as msg:
            logging.debug('{:14} : {}'.format(host, msg))

def socket_gethostbyname_ex():
    """
    for access to more naming information about a server, use `gethostname_ex()`
    
    it returns the canonical hostname of the server, any aliases, 
    and all of the available IP addresses that can be used to reach it.
    """
    HOSTS = [
        'apu',
        'pymotw.com',
        'www.python.org',
        'nosuchname',
    ]

    for host in HOSTS:
        logging.debug(f'{host}')
        try:
            """
            ! Q: wtf is this _ex meaning tho?
            * A: ex(tra)?
            """
            name, aliases, addresses = socket.gethostbyname_ex(host)
            logging.debug('  hostname: {}'.format(name))
            logging.debug('  aliases : {}'.format(aliases))
            logging.debug(' Addresses: {}'.format(addresses))
        except socket.error as msg:
            logging.debug('ERROR : {}'.format(msg))

def socket_getfqdn():
    for host in ['apu', 'pymotw.com']:
        logging.debug('{:>10} : {}'.format(host, socket.getfqdn(host)))

def socket_gethostbyaddr():
    hostname, aliases, addresses = socket.gethostbyaddr('10.9.0.10')
    logging.debug('Hostname :   {}'.format(hostname))
    logging.debug('Aliases  :   {}'.format(aliases))
    logging.debug('Addresses:   {}'.format(addresses))
    ...

if __name__ == "__main__":
    # socket_gethostname()
    # socket_gethostbyname()
    # socket_gethostbyname_ex()
    # socket_getfqdn()
    socket_gethostbyaddr()