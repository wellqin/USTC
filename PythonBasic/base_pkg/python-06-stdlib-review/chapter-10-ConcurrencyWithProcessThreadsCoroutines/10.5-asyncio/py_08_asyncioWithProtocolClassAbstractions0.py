"""
up to this point, the examples have all avoid mingling concurrency and I/O operations 
to focus on one concept at a time.

however, switching contexts when I/O blocks is one of the primary use cases for asyncio.

building on the concurrency concepts introduced earlier,
this section examine two sample programs that implement a simple echo server and client,
similar to the examples used in the `socket` and `socketserver` sections.

a client can connect to the server, send some data,
and then receive the same data as a response.

each time an I/O operation is initiated, the executing code gives up controls to the event loop,
allowing other tasks to run until the I/O is ready.

sample code:
asyncio_echo_client_protocol.py
asyncio_echo_server_protocol.py
"""