import asyncio


async def my_coroutine(fut):
    fut.set_result("Future is done!")


async def main():
    # fut = asyncio.Future()
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    fut.add_done_callback(lambda fut: print("Future is done!", fut))
    print("Future is created")
    task = asyncio.create_task(my_coroutine(fut))
    print("Task is created")
    await fut
    print(fut.result())


asyncio.run(main())
