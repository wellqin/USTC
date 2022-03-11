"""
! wtf is a network?
a network is defined by a range of addresses.

it is usually expressed with a base addresses
and a mask indicating which portions of the address represent the network,
and which portions represent addresses on that network.

the mask can be expressed either explicitly or by using a prefix length value,
as in the following example.

"""

import ipaddress
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s'
)

def ipaddress_networks():
    NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
    ]

    for n in NETWORKS:
        """
        as with addresses, there are two network classes for IPv4 and IPv6 networks.
        
        each class provides properties or methods for accessing values associated with the network,
        such as the broadcast address and the addresses on the network available for hosts to use.
        """
        net = ipaddress.ip_network(n)
        logging.debug('{!r}'.format(net))
        logging.debug('     is private: {}'.format(net.is_private))
        logging.debug('      broadcast: {}'.format(net.broadcast_address))
        logging.debug('     compressed: {}'.format(net.compressed))
        logging.debug('   with netmask: {}'.format(net.with_netmask))
        logging.debug('  with hostmask: {}'.format(net.with_hostmask))
        logging.debug('  num addresses: {}'.format(net.num_addresses))
        logging.debug('{}'.format('-'*50))

if __name__ == "__main__":
    ipaddress_networks()
    