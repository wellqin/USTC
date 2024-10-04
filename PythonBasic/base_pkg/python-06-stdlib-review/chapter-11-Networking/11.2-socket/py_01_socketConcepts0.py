"""
Addressing, Protocol Families, and Socket Types

a `socket` is one endpoint of a communication channel used by programmers to pass data back and forth locally
or across the Internet.

sockets have two primary properties controlling the way they send data.
|-- the `address family` controls the OSI network layer protocol used and 
|-- the `socket type` controls the transport leyer protocol.

Python supports theree address families.
|-- AF_INET, is used for IPv4 Internettt addressing.
|   IPv4 addresses are 4 bytes longing and are usually represented as a sequence of four numbers, one per octet, separated by dots(e.g., 10.1.1.5 and 127.0.0.1)
|
|-- AF_INET6, is used for IPv6 Internet addressing. 
|   IPv6 is the "next generation" version of the Internet protocol, and supports 128-bit addresses, traffic shaping, and routing features not available under IPv4.
|
|-- AF_UNIX is the address family for Unix Domain Sockets(UDS), an interprocess communication protocol available on POSIX-compliant systems.
|   The implementation of UDS typically allows the operating system to pass data directly from process to process, w/o going through the network stack.
|   NOTE: AF_UNIX constant is defined only on systems where UDS is supported.

the socket type
|-- SOCK_DGRAM for message-oriented datagram transport.
|   Datagram sockets are most often associated with UDP, the `user datagram protocol`
|   they provide unreliable delivery of individual messages.
|
|-- SOCK_STREAM for stream-oriented transport.
|   Stream-oriented sockets are associated with TCP, the `transmission control protocol`

most application protocols that deliver a large amount of data, such as HTTP, are built on top of TCP
because it is simpler to create complex applications when message ordering and delivery are handled automatically.

UDP is commonly used for protocols where order is less important
(since the messages are self-contained and often small, such as name lookups via DNS)
and for `multicasting` (sending the same data to several hosts).

Both UDP and TCP can be used with either IPv4 or IPvv6 addressing.
"""