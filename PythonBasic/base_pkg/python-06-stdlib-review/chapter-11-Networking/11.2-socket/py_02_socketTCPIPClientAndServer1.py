"""
sockets can be confirmed to act as a server and listen for incoming messages,
or they can connect to other applications as a client.

after both ends of a TCP/IP socket are connected, 
communication is bidirectional.
"""
import socket, logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def socket_echo_server():
    # creates a TCP/IP socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binds the socket to the port.
    server_address = ('localhost', 10_000)
    logging.debug('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    # listens for incoming connections
    sock.listen(1)

    while True:
        # wait for a connection
        logging.debug('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            logging.debug('connection from {}'.format(client_address))
            # receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                logging.debug('received {!r}'.format(data))
                if data:
                    logging.debug('sending data back to the client')
                    connection.sendall(data)
                else:
                    logging.debug('no data from {}'.format(client_address))
                    break
        finally:
            # clean up the connection
            connection.close()


if __name__ == "__main__":
    """
    OSError
    ? Q: why the fuck error happends? 
    * A: https://help.socketlabs.com/docs/how-to-fix-error-only-one-usage-of-each-socket-address-protocolnetwork-addressport-is-normally-permitted
    
    If you see the error, "Only one usage of each socket address (protocol/network address/port) is normally permitted" in the logs when a connection is being made, 
    it means that you are exhausting all the available network ports on the machine. 
    
    By default the OS only has around 4000 ports available that are not reserved by the system. 
    What happens is that when any network connection is closed it goes into a TIME_WAIT state for 240 seconds and cannot be reused until this wait state is over.

    As an example, if there are 16 connections per second for 4 minutes (16*4*60=3840), you will exhaust all the ports shortly there after. 
    Now if you have HAS and the MTA on the same machine, this will get exhausted a lot sooner because in addition to them communicating with each other, 
    which uses 2 ports (one for the MTA and one for HAS), the MTA uses up a lot of ports sending the mail.

    You can fix this by modifying the below values.
    - One of the ways is to increase the dynamic port range. The max by default is 5000. 
      You can set this up to 65534. HKLMSystemCurrentControlSetServicesTcpipParametersMaxUserPort is the key to use.

    - The second thing you can do is, once the connection does get into an TIME_WAIT state, you can reduce the time it is in that state. 
      Default is 4 minutes, but you can set this to 30 seconds. HKLMSystemCurrentControlSetServicesTcpipParametersTCPTimedWaitDelay is the key to use.

    After these changes are made the system must be restarted.    
    """
    socket_echo_server()

