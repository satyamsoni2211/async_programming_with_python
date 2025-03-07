import asyncio


async def sleep_routine(n=1):
    print(f"Sleeping for 1 second... from {n}")
    await asyncio.sleep(1)  # supports async and is non blocking
    print("Done sleeping!")


async def main():
    task1 = asyncio.create_task(sleep_routine(2))
    task2 = asyncio.create_task(sleep_routine(1))
    # you do not need to schedule coroutine manually using await
    task1.add_done_callback(lambda future: print("Task 1 done!"))
    # await asyncio.wait_for(task1,0.5)
    await asyncio.wait([task1, task2], return_when=asyncio.FIRST_COMPLETED)


asyncio.run(main())
