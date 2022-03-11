import socket, logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def socket_echo_client_easy():
    def get_constants(prefix):
        return {
            getattr(socket, n): n
            for n in dir(socket)
            if n.startswith(prefix)
        }

    families = get_constants('AF_')
    types = get_constants('SOCK_')
    protocols = get_constants('IPPROTO_')
    
    # creates a TCP/IP socket
    addr = ('localhost', 10_000)
    sock = socket.create_connection(addr)
    logging.debug('Family   : {}'.format(families.get(sock.family, None)))
    logging.debug('Type     : {}'.format(types.get(sock.type, None)))
    logging.debug('Protocol : {}'.format(protocols.get(sock.proto, None)))
    logging.debug(f'{"-" * 50}')
    try:
        # Send data.
        message = b'This is the message. It will be repeated.'
        logging.debug('sending {!r}'.format(message))
        sock.sendall(message)
        
        amount_received = 0
        amount_expected = len(message)
        # receive data.
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            logging.debug('received {!r}'.format(data))
    finally:
        logging.debug('closing socket')
        sock.close()

if __name__ == "__main__":
    socket_echo_client_easy()