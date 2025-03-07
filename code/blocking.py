import asyncio
from time import sleep, time
import threading


async def nonblocking(arg):
    t1 = time()
    print(f"Running in foo from {arg}")
    await asyncio.sleep(1)
    print(f"thread id: {threading.get_ident()}")
    print(f"Explicit context switch to foo again from {arg}")
    t2 = time()
    print(f"Time taken for non blocking {arg}: {t2 - t1}")


def blocking(arg):
    t1 = time()
    print(f"Explicit context to blocking from {arg}")
    sleep(1)
    print(f"thread id: {threading.get_ident()}")
    print(f"Implicit context switch back to blocking from {arg}")
    t2 = time()
    print(f"Time taken for blocking {arg}: {t2 - t1}")


async def main():
    # asyncio.to_thread(blocking,"b1")
    loop = asyncio.get_running_loop()
    awaitables = [
        nonblocking("nb1"),
        nonblocking("nb2"),
        loop.run_in_executor(None, blocking, "b1"),
    ]
    await asyncio.gather(*awaitables)


asyncio.run(main())
