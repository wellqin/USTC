import binascii
import ipaddress
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s'
)

def ipaddress_addresses():
    ADDRESSES = [
        '10.9.0.6',
        'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
    ]

    for ip in ADDRESSES:
        addr = ipaddress.ip_address(ip)
        logging.debug('{!r}'.format(addr))
        logging.debug('     IP version: {}'.format(addr.version))
        logging.debug('     is private: {}'.format(addr.is_private))
        logging.debug('    packed form: {}'.format(binascii.hexlify(addr.packed)))
        logging.debug('        integer: {}'.format(int(addr)))
        logging.debug('{}'.format('-'*50))

if __name__ == "__main__":
    ipaddress_addresses()