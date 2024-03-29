import socket
import os
"""
The `socketpair()` function is useful for setting up UDS sockets for interprocess communication under Unix. 
It creates a pair of connected sockets that can be used to communicate
between a parent process and a child process after the child is forked.
"""
parent, child = socket.socketpair()
pid = os.fork()
if pid:
    print('in parent, sending message')
    child.close()
    parent.sendall(b'ping')
    response = parent.recv(1024)
    print('response from child:', response)
    parent.close()
else:
    print('in child, waiting for message')
    parent.close()
    message = child.recv(1024)
    print('message from parent:', message)
    child.sendall(b'pong')
    child.close()
