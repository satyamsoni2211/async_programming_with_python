import asyncio


async def gen():
    for i in range(10):
        yield i


async def main():
    async for i in gen():
        print(i)


asyncio.run(main())
