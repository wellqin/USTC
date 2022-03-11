"""
using the coroutine `getaddrinfo()` to convert a hostname and port number to an IP or IPv6 address.
As with the version of the function in the `socket` module,
the return value is a list of tuples containing five pieces of information:

    index, result
- 0, The address family
- 1, The address type
- 2, The protocol
- 3, The canonical name for the server
- 4, A socket address tuple suitable for opening a connection to the server on the port originally specified

Queries can be filtered by protocol.
In the following example, a filter ensure that only TCP reponses are returned.
"""

import asyncio
import logging
import socket
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_getaddrinfo():
    ### * interesting. only Domain Server Names work well. NOT webpages.
    TARGETS = [
        ('github.com', 'https'),
        ('docs.python.org', 'https'),
        ('wiki.guildwars2.com', 'https'),
    ]

    async def main_job(loop, targets):
        for target in targets:
            info = await loop.getaddrinfo(
                *target,
                proto=socket.IPPROTO_TCP,   # ? after commentout this line, output has no f*cking difference
            )
            for host in info:
                logging.debug('{:20}:   {}'.format(target[0], host[4][0]))

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(event_loop, TARGETS))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_getaddrinfo()