import asyncio
import threading


async def foo():
    print("Running in foo")
    await asyncio.sleep(1)
    print(f"thread id: {threading.get_ident()}")
    print("Explicit context switch to foo again")


async def bar():
    print("Explicit context to bar")
    await asyncio.sleep(1)
    print(f"thread id: {threading.get_ident()}")
    print("Implicit context switch back to bar")


async def main():
    tasks = [foo(), bar()]
    await asyncio.gather(*tasks)


asyncio.run(main())
