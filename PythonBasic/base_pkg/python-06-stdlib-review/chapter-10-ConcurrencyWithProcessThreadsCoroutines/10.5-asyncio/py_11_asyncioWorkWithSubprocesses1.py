"""
unix-like os code sample.

i feel personally attacked even i have one unix-like mac

sample code in the book is NOT working. SKIP @ZL

P699-714
"""

import asyncio
import functools
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class DFProtocol(asyncio.SubprocessProtocol):
    FD_NAMES = ['stdin', 'stdout', 'stderr']
    def __init__(self, done_future):
        self.done   = done_future
        self.buffer = bytearray()
        super().__init__()

    def connection_made(self, transport):
        logging.debug('process started {}'.format(transport.get_pid()))
        self.transport = transport
        
    def pipe_data_received(self, fd, data):
        logging.debug('read {} bytes from {}'.format(len(data), self.FD_NAMES[fd]))
        if fd == 1:
            self.buffer.extend(data)
    def process_exited(self):
        logging.debug('process exited')
        return_code = self.transport.get_returncode()
        logging.debug('reutrn code {}'.format(return_code))
        if not return_code:
            cmd_output = bytes(self.buffer).decode()
            results    = self._parse_results(cmd_output)
        else:
            results    = []
        self.done.set_result((return_code, results))
    def _parse_results(self, output):
        logging.debug('parsing results')
        if not output:
            return []
        lines   = output.splitlines()
        headers = lines[0].split()
        devices = lines[1:]
        results = [
            dict(zip(headers, line.split()))
            for line in devices
        ]
        return results

async def run_df(loop):
    logging.debug('in run_df')
    cmd_done = asyncio.Future(loop=loop)
    factory  = functools.partial(DFProtocol, cmd_done)
    proc     = loop.subprocess_exec(
        factory,
        'df', '-hl',
        stdin=None,
        stderr=None,
    )
    try:
        logging.debug('launching process')
        transport, protocol = await proc
        logging.debug('waiting for process to complete')
        await cmd_done
    finally:
        transport.close()
    return cmd_done.result()

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(run_df(event_loop))
finally:
    event_loop.close()

if return_code:
    logging.debug('error exit {}'.format(return_code))
else:
    logging.debug('\ndir:')
    for result in results:
        logging.debug('{}'.format(result))