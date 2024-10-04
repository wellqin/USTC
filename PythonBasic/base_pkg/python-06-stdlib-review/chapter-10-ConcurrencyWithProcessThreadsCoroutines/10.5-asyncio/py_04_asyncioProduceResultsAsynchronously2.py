import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_future_await():
    ### a normal action marks a Future obj as "done"
    def mark_done(future, result):
        logging.debug('setting future result to {!r}'.format(result))
        future.set_result(result)
    ### a coroutine as main job
    async def main_job(loop):
        all_done = asyncio.Future()
        logging.debug('scheduling mark_done')
        loop.call_soon(mark_done, all_done, 'the result @ set by ZL')
        result = await all_done
        logging.debug('return result: {!r}'.format(result))
        pass

    event_loop = asyncio.get_event_loop()
    try:
        result = event_loop.run_until_complete(main_job(event_loop))
        logging.debug(f'result: {result}')
    finally:
        event_loop.close()

if __name__ == "__main__":
    # Future() obj.await()
    asyncio_future_await()