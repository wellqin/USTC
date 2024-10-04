import socket, logging
import struct, binascii
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def socket_address_packing():
    for string_address in ['192.168.1.1', '127.0.0.1']:
        """
        always pairs.
        IPv4
        socket.inet_aton()
        socket.inet_ntoa()
        """
        packed = socket.inet_aton(string_address)
        logging.debug('Original : {}'.format(string_address))
        logging.debug('Packed   : {}'.format(binascii.hexlify(packed)))
        logging.debug('Unpacked : {}'.format(socket.inet_ntoa(packed)))
        logging.debug(' ' * 50)

def socket_ipv6_address_packing():
        """
        always pairs.
        IPv6
        socket.inet_pton()
        socket.inet_ntop()
        """
        string_address = '2002:ac10:10a:1234:21e:52ff:fe74:40e'
        packed         = socket.inet_pton(socket.AF_INET6, string_address)
        logging.debug('Original : {}'.format(string_address))
        logging.debug('Packed   : {}'.format(binascii.hexlify(packed)))
        logging.debug('Unpacked : {}'.format(socket.inet_ntop(socket.AF_INET6, packed)))

if __name__ == "__main__":
    # IPv4
    socket_address_packing()
    # IPv6
    socket_ipv6_address_packing()