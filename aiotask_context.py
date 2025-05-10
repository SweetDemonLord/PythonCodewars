import asyncio
import sys
import aiotask_context as context


async def indication(timeout):
    while True:
        print(context.get('symbol'), end='')
        sys.stdout.flush()
        await asyncio.sleep(timeout)


async def sleep(t, indication_t, symbol='.'):
    loop = asyncio.get_event_loop()

    context.set(key='symbol', value=symbol)
    loop.create_task(indication(indication_t))
    await asyncio.sleep(t)


loop = asyncio.get_event_loop()
loop.set_task_factory(context.task_factory)
loop.run_until_complete(asyncio.gather(
    sleep(1, 0.1, '0'),
    sleep(1, 0.1, 'a'),
    sleep(1, 0.1, 'b'),
    sleep(1, 0.1, 'c'),
))