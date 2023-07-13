import asyncio, time

# async def func1():
#     print("%%%%%%%%%%%%%%%%%%")
#     # time.sleep(3)
#     await asyncio.sleep(3)
#     print("%%%%%%%%%%%%%%%%%%")

# async def func2():
#     print("++++++++++++++++++")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("++++++++++++++++++")

# async def func3():
#     print("===================")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("===================")
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]
#     asyncio.run(asyncio.wait(tasks))

async def func1():
    print("%%%%%%%%%%%%%%%%%%")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("%%%%%%%%%%%%%%%%%%")

async def func2():
    print("++++++++++++++++++")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("++++++++++++++++++")

async def func3():
    print("===================")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("===================")
async def main():
    # first
    # f1 = func1()
    # await f1
    # second
    tasks = [asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())

