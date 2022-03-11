import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_future_event_loop():
    # Future object reperents the result of work that has not been completed yet.
    # a normal function marks Future obj as "done"
    def mark_done(future, result):
        logging.debug('setting future result to {!r}'.format(result))
        future.set_result(result)
    
    # create event loop
    event_loop = asyncio.get_event_loop()
    try:
        ### creates a Future object
        all_done = asyncio.Future()
        logging.debug('scheduling mark_done')
        ### registers this "mark" action into event loop 
        event_loop.call_soon(mark_done, all_done, 'the result')
        logging.debug('entering event loop')
        result = event_loop.run_until_complete(all_done)
        logging.debug('return result: {!r}'.format(result))
    finally:
        logging.debug('existing event loop')
        event_loop.close()
    logging.debug('future result: {!r}'.format(all_done.result()))

if __name__ == "__main__":
    ### this is actually simple .. 
    ### ! all it does is mark "done" on a Future object
    asyncio_future_event_loop()