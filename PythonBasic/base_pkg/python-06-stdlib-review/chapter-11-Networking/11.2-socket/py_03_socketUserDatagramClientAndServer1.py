"""
mechnism

Table: UDP vs TCP/IP
+-------------------+-------------------------------+--------------------------------------+
|                   | TCP/IP                        | UDP                                  |
+===================+===============================+======================================+
| short for?        | transmission control protocol | user datagram protocol               |
+-------------------+-------------------------------+--------------------------------------+
| do what?          | stream-oriented protocol      | message-oriented protocol            |
+-------------------+-------------------------------+--------------------------------------+
| require           | Yes                           | No                                   |
| long-lived conn?  |                               |                                      |
+-------------------+-------------------------------+--------------------------------------+
| must fit w/i a    | No                            | Yes                                  |
| signle datagram?  |                               |                                      |
| 65,535-byte packet|                               |                                      |
+-------------------+-------------------------------+--------------------------------------+

"""

import socket
import sys
# Create a UDP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port.
server_address = ('localhost', 10_000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)
    print('received {} bytes from {}'.format(
    len(data), address))
    print(data)
    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(sent, address))
