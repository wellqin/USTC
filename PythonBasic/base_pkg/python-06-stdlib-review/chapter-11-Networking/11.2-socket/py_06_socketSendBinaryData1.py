"""
Sockets transmit streams of bytes. Those bytes can contain text messages encoded as bytes,
as in the previous examples, 

or they can be made up of binary data that has been packed
into a buffer with struct (page 117) to prepare it for transmission.

"""

import binascii
import socket
import struct
import sys
# Create a TCP/IP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

values = (1, b'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)
print('values =', values)
try:
    # Send data.
    print('sending {!r}'.format(binascii.hexlify(packed_data)))
    sock.sendall(packed_data)
finally:
    print('closing socket')
    sock.close()
