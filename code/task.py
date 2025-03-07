import asyncio
import time

async def sleep_routine(n=1):
    print(f'Sleeping for 1 second... from {n}')
    await asyncio.sleep(1) # supports async and is non blocking 
    print('Done sleeping!')

# async def main():
#     print('Hello, world!')
#     t1 = time.time()
#     task1 = asyncio.create_task(sleep_routine(2))
#     # you do not need to schedule coroutine manually using await 
#     task1.add_done_callback(lambda future: print('Task 1 done!'))
#     await sleep_routine(1)
#     t2 = time.time()
#     print(f'Time taken: {t2-t1}')

async def main():
    print('Hello, world!')
    t1 = time.time()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(sleep_routine(2))
        tg.create_task(sleep_routine(1))
    await sleep_routine(3)
    t2 = time.time()
    print(f'Time taken: {t2-t1}')

asyncio.run(main())