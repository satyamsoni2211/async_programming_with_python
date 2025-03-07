import asyncio


async def main():
    print("Hello, world!")


asyncio.run(main())
# main() # cannot run this coroutine directly

# alternative way to run the coroutine
# created an event loop
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
