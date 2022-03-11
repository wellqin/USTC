import sys, codecs
sys.path.append('.')
from pkg.breaker import addBreaker
import socketserver, threading, socket

class Echo(socketserver.BaseRequestHandler):
    def handle(self):
        # get some bytes and echo them back to the client
        data = self.request.recv(1024)
        self.request.send(data)
        return

class PassThrough:
    def __init__(self, other):
        self.other = other
    def write(self, data):
        print('Writing  :', repr(data))
        return self.other.write(data)
    def read(self, size=-1):
        print('Reading  :', end=' ')
        data = self.other.read(size)
        print(repr(data))
        return data
    def flush(self):
        return self.other.flush()
    def close(self):
        return self.other.close()
    
@addBreaker
def codecs_socket_fail():
    address     = ('localhost', 0)  # let the kernel assign a port
    server      = socketserver.TCPServer(address, Echo)
    ip, port    = server.server_address # which port was assigned?

    t    = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)   # don't hang on exit
    t.start()

    # connect to the server
    s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send the data
    # wrong: NOT encoded first!
    text      = 'français'
    len_sent  = s.send(text)
    # receive a response
    response  = s.recv(len_sent)
    print(repr(response))
    # clean up
    s.close()
    server.socket.close()
    pass

@addBreaker
def codecs_socket_pass():
    address  = ('localhost', 0)
    server   = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    read_file  = s.makefile('rb')
    incoming   = codecs.getreader('utf8')(PassThrough(read_file))
    write_file = s.makefile('wb')
    outgoing   = codecs.getwriter('utf8')(PassThrough(write_file))

    # send data
    text = 'français'
    print('Sending  :', repr(text))
    outgoing.write(text)
    outgoing.flush()

    response = incoming.read()
    print('Received :', repr(response))
    s.close()
    server.socket.close()
    pass


if __name__ == "__main__":
    # ! network sockets are `byte streams`, and unlike the standard input and out streams,
    # ! they do not support encoding by default
    # * thus, programs that want to send or receive unicode data over the netweork must encode the data into bytes
    # * before it is written to a socket
    # codecs_socket_fail()
    # pass
    codecs_socket_pass()