import selectors
import socket
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

mysel = selectors.DefaultSelector()
keep_running = True

def read(connection, mask):
    """
    callback for read events
    """
    global keep_running

    client_address = connection.getpeername()
    logging.debug('read({})'.format(client_address))
    data = connection.recv(1024)
    if data:
        logging.debug('     received {!r}'.format(data))
        connection.sendall(data)
    else:
        logging.debug('     closing')
        mysel.unregister(connection)
        connection.close()
        keep_running = False

def accept(sock, mask):
    """
    call back for new connections
    """
    new_connection, addr = sock.accept()
    logging.debug('accept({})'.format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)

server_address = ('localhost', 10_000)
logging.debug('starting up on {} port {}'.format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

mysel.register(server, selectors.EVENT_READ, accept)

while keep_running:
    logging.debug('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        callback = key.data
        callback(key.fileobj, mask)
logging.debug('shutting down')
mysel.close()


"""
? Q: do we really need this low-level thing?
? A: i doubt too. if we are using this low-level things, we may use C/C++ directly

P764 - 790, SKIP, @ZL, 20200904
"""