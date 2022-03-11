"""
pairs

loop.getaddrinfo() vs loop.getnameinfo()

"""

import asyncio, logging, socket, sys

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def asyncio_getnameinfo():
    TARGETS = [
        ('52.74.223.119', 443),
        ('151.101.76.223', 443),
        ('34.203.47.116', 443),
        ('3.213.213.110', 443),
        ('34.200.30.227', 443),
    ]

    async def main_job(loop, targets):
        for target in targets:
            info = await loop.getnameinfo(target)
            logging.debug('{:15}: {} {}'.format(target[0], *info))
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(event_loop, TARGETS))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_getnameinfo()