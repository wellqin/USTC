"""
Point-to-point connections suffice for many communication needs, but passing the same
information between many peers becomes increasingly more challenging as the number of
direct connections grows. 

Sending messages separately to each recipient consumes additional
processing time and bandwidth, which can be a problem for applications that perform
operations such as streaming video or audio. 

Using `multicast` to deliver messages to more
than one endpoint at a time achieves better efficiency because the network infrastructure
ensures that the packets are delivered to all recipients.


Multicast messages are always sent using UDP, since TCP assumes a pair of communicating systems are present. The addresses used for multicast, called multicast groups, are a
subset of the regular IPv4 address range (224.0.0.0 through 230.255.255.255) that have been
reserved for multicast traffic. These addresses are treated specially by network routers and
switches, so messages sent to the group can be distributed over the Internet to all recipients
that have joined the group.

"""

import socket
import struct
import sys
message = b'very important data'
multicast_group = ('224.3.29.71', 10000)
# Create the datagram socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
sock.settimeout(0.2)
# Set the time-to-live for messages to 1 so they do not
# go past the local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
try:
    # Send data to the multicast group.
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)
    # Look for responses from all recipients.
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received {!r} from {}'.format(data, server))
finally:
    print('closing socket')
    sock.close()
