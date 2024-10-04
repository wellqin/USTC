import asyncio, logging, sys

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

SERVER_ADDRESS = ('localhost', 10000)

log = logging.getLogger('main')
event_loop = asyncio.get_event_loop()

class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.address   = transport.get_extra_info('peername')
        self.log       = logging.getLogger(
            'EchoServer_{}_{}'.format(*self.address)
        )
        self.log.debug('connection accepted')

    def data_received(self, data):
        self.log.debug('received {!r}'.format(data))
        self.transport.write(data)
        self.log.debug('sent {!r}'.format(data))
    
    def eof_received(self):
        self.log.debug('received EOF')
        if self.transport.can_Write_eof():
            self.transport.write_eof()

    def connection_lost(self, error):
        if error:
            self.log.error('ERROR: {}'.format(error))
        else:
            self.log.debug('closing')
        super().connection_lost(error)

# creates the server and lets the loop finish the coroutine before starting the real event loop
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server  = event_loop.run_until_complete(factory)
log.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))
# enters the event loop permantly to handle all connections
try:
    event_loop.run_forever()
finally:
    log.debug('closing server')
    server.close()
    event_loop.run_until_complete(server.wait_close())
    log.debug('closing event loop')
    event_loop.close()