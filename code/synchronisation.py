import asyncio

async def sleep_routine(n=1, semaphore=None):
    async with semaphore:
        print(f'Sleeping for 1 second... from {n}')
        await asyncio.sleep(1) # supports async and is non blocking 
        print('Done sleeping!')

async def main():
    semaphore = asyncio.Semaphore(10)
    awaitables = []
    for i in range(100):
        awaitables.append(sleep_routine(i, semaphore))
    await asyncio.gather(*awaitables)

asyncio.run(main())