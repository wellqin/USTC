import ipaddress
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def ipaddress_interfaces():
    ADDRESSES = [
        '10.9.0.6/24',
        'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64',
    ]

    for ip in ADDRESSES:
        """

        ? wtf do these glossaries mean in real life or just concepts?
        ip_address()
        ip_network()
        ip_interface()

        netmask
        hostmask

        ! i lack knowladge about network, fml!
        """
        iface = ipaddress.ip_interface(ip)
        logging.debug('{!r}'.format(iface))
        logging.debug('network:\n   {}'.format(iface.network))
        logging.debug('ip:\n    {}'.format(iface.ip))
        logging.debug('IP with prefixlen:\n {}'.format(iface.with_prefixlen))
        logging.debug('netmask:\n   {}'.format(iface.with_netmask))
        logging.debug('hostmask:\n  {}'.format(iface.with_hostmask))
        logging.debug(f'{"-" * 20}')

if __name__ == "__main__":
    ipaddress_interfaces()