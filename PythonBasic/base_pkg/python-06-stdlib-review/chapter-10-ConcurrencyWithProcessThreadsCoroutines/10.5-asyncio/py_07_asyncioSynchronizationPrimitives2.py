import asyncio, logging, functools

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_event():
    """
    思う通りか

    an `asyncio.Event` is based on a `threading.Event`.
    it allows multiple consumers to wait for sth to happen 
    w/o looking for a specific value to be assiciated with the notification
    ! aha! event just like `user-defined cutoff timeline
    ! yeah, `asyncio.Event` behavior is similar with `asyncio.Lock`
    
    Table: asyncio.Event vs asyncio.Lock vs asyncio.Condition
    +---------------------------------------+-------------------+---------------+------------------------------------------+
    | diff                                  | asyncio.Event     | asyncio.Lock  | asyncio.Condition                        |
    +=======================================+===================+===============+==========================================+
    | start as soon as Event/Lock changes?  | yes               | no            | yes                                      |
    +---------------------------------------+-------------------+---------------+------------------------------------------+
    | need to acquire a unique Event/Lock?  | no                | yes           | no                                       |
    +---------------------------------------+-------------------+---------------+------------------------------------------+
    | notify all waiting coroutines?        | yes               | yes           | no, controlled with an arg to `notify()` |
    +---------------------------------------+-------------------+---------------+------------------------------------------+

    """
    def set_event(event):
        logging.debug('setting event in callback')
        event.set()
    async def coro1(event):
        logging.debug('coro1 waiting for event')
        await event.wait()
        logging.debug('coro1 triggered')
    async def coro2(event):
        logging.debug('coro2 waiting for event')
        await event.wait()
        logging.debug('coro2 triggered')
    async def main_job(loop):
        # create a shared event
        event = asyncio.Event()
        logging.debug('event start state: {}'.format(event.is_set()))
        loop.call_later(.1, functools.partial(set_event, event))
        await asyncio.wait([
            coro1(event),
            coro2(event),
        ])
        logging.debug('event end state: {}'.format(event.is_set()))

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        event_loop.close()

if __name__ == "__main__":
    asyncio_event()