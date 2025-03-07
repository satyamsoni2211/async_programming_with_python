import asyncio
import time

async def sleep_routine(n=1):
    print(f'Sleeping for 1 second... from {n}')
    await asyncio.sleep(1) # supports async and is non blocking 
    print('Done sleeping!')

async def main():
    print('Hello, world!')
    t1 = time.time()
    # await sleep_routine(1)
    # await sleep_routine(2)
    awaitables = [sleep_routine(1), sleep_routine(2)]
    await asyncio.gather(*awaitables) # wraps your coroutine into task
    t2 = time.time()
    print(f'Time taken: {t2-t1}')

asyncio.run(main())