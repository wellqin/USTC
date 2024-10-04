"""
aha, socket module is like a simple telephone framework.

it bridges sender and receiver over time and space.

"""

import socket, logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def socket_echo_client():
    # creates a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connects the socket to the port where the server is listening
    server_address = ('localhost', 10_000)
    logging.debug('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    try:
        # send data
        message = b'this is the message. It will be repeated.'
        logging.debug('sending {!r}'.format(message))
        sock.sendall(message)
        # look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            logging.debug('received {!r}'.format(data))
    finally:
        logging.debug('closing socket')
        sock.close()


if __name__ == "__main__":
    socket_echo_client()