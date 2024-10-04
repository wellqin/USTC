import ipaddress
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def ipaddress_network_iterate():
    NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
    ]

    for n in NETWORKS:
        net = ipaddress.ip_network(n)
        logging.debug('{!r}'.format(net))

        """
        a network instance is iterable 
        and yields the addresses on the network.
        """
        for _, ip in zip(range(3), net):
            logging.debug(f'{ip}')
        logging.debug(f'{"-"*20}')


def ipaddress_network_iterate_hosts():
    NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',        
    ]

    for n in NETWORKS:
        net = ipaddress.ip_network(n)
        logging.debug('{!r}'.format(net))
        """
        iterating over the network yields addresses,
        but not all of them are valid for hosts.

        for example, the base address of the network and the broadcast address are both included.

        To find the addresses that can be used by regular hosts on the network, use the hosts() method,
        which produces a generator. 
        """
        for _, ip in zip(range(3), net.hosts()):
            logging.debug(f'{ip}')
        logging.debug(f'{"-" * 20}')

def ipaddress_network_membership():
    NETWORKS = [
        ipaddress.ip_network('10.9.0.0/24'),
        ipaddress.ip_network('fdfd:87b5:b475:5e3e::/64'),
    ]

    ADDRESSES = [
        ipaddress.ip_address('10.9.0.6'),
        ipaddress.ip_address('10.7.0.31'),
        ipaddress.ip_address(
            'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'
        ),
        ipaddress.ip_address('fe80::3840:c439:b25e:63b0'),
    ]
    for ip in ADDRESSES:
        for net in NETWORKS:
            """
            in addition to the iterator protocol, 
            networks support the `in` operator, which is used to determine whether an address is part of a network

            ! mechnism
            the implementation of `in` uses the network mask to test the address,
            so it is much more effecient than expanding the full list of addresses on the network.
            """
            if ip in net:
                logging.debug('{}\nis on {}'.format(ip, net))
                break
        else:
            logging.debug('{}\nis not on a known network'.format(ip))
        logging.debug(f'{"-" * 20}')

if __name__ == "__main__":
    ipaddress_network_iterate()
    ipaddress_network_iterate_hosts()
    ipaddress_network_membership()