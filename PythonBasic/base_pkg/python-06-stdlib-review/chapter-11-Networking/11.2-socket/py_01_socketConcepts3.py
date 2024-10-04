import socket, logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def socket_getaddrinfo():
    def get_constants(prefix):
        return {
            getattr(socket, n):n
            for n in dir(socket)
            if n.startswith(prefix)
        }

    families  = get_constants('AF_')
    types     = get_constants('SOCK_')
    protocols = get_constants('IPPROTO_')
    homepage  = ('www.python.org', 'http')
    """
    socket.getaddrinfo() takes several arguments for filtering the result list.
    the `host` and `port` values given in the example are required arguments.
    the optional args are `family`, `socktype`, `proto`, and `flags`.
    the optional values should be either 0 or one of the constants defined by `socket`. 
    """
    for response in socket.getaddrinfo(*homepage):
        # unpacks the response tuple
        family, socktype, proto, canonname, sockaddr = response
        logging.debug('Family         : {}'.format(families.get(family, None)))
        logging.debug('Type           : {}'.format(types.get(socktype, None)))
        logging.debug('Protocol       : {}'.format(protocols.get(proto, None)))
        logging.debug('Canonical name : {}'.format(canonname))
        logging.debug('Socket address : {}'.format(sockaddr))
    logging.debug(f'{"-" * 50}')

def socket_getaddrinfo_extra_args():
    def get_constants(prefix):
        return {
            getattr(socket, n): n
            for n in dir(socket)
            if n.startswith(prefix)
        }
    families    = get_constants('AF_')
    types       = get_constants('SOCK_')
    protocols   = get_constants('IPPROTO_')

    responses   = socket.getaddrinfo(
        host='www.python.org',
        port='http',
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
        flags=socket.AI_CANONNAME,
    )

    for response in responses:
        # unpacks the response tuple,
        family, socktype, proto, canonname, sockaddr = response
        logging.debug('Family           : {}'.format(families.get(family, None)))
        logging.debug('Type             : {}'.format(types.get(socktype, None)))
        logging.debug('Protocol         : {}'.format(protocols.get(proto, None)))
        logging.debug('Canonical name   : {}'.format(canonname))
        logging.debug('Socket address   : {}'.format(sockaddr))
    logging.debug(f'{"-" * 50}')


if __name__ == "__main__":
    socket_getaddrinfo()
    socket_getaddrinfo_extra_args()