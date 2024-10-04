import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_coroutine_return():
    async def coroutine():
        logging.debug(f'in coroutine')
        return 'result' #<~ r u fcking kidding me?!

    event_loop = asyncio.get_event_loop()

    try:
        #<~ Q: do u see the difference here? hmmm, parenthesis
        #<~ A: sry mate, nothing. mb.
        #<~ it means 生产计划员可以制定生产计划、获取生产实际结果. 只需制定计划(coroutine)并填入“计划” event_loop
        return_value = event_loop.run_until_complete(coroutine())
        logging.debug('it returned: {!r}'.format(return_value))
    finally:
        event_loop.close()  # <~ this is fcking stupid isn't it? shoud use context manager here

if __name__ == "__main__":
    asyncio_coroutine_return()