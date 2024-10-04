"""
wait a second.
do we really do this?

mechnism

From the programmer’s perspective, there are two essential differences between using a Unix
domain socket and an TCP/IP socket. 

First, the address of the socket is a path on the file system, 
rather than a tuple containing the server name and port. 

Second, the node created in the file system to represent the socket persists after the socket is closed, 
so it needs to be removed each time the server starts. 

"""

import socket
import sys
import os
server_address = './uds_socket'
# Make sure the socket does not already exist.
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise
# Create a UDS socket.
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
# Bind the socket to the address.
print('starting up on {}'.format(server_address))
sock.bind(server_address)
# Listen for incoming connections.
sock.listen(1)

while True:
    # Wait for a connection.
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it.
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        # Clean up the connection.
        connection.close()

