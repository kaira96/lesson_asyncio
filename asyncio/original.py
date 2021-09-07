# pip (pip3) install aiohttp


# План:
# 1. Asyncio фреймворк для создания событийных циклов
# 2. Пример простой асинхронной программы времён Python 3.4
# 3. Синтаксис Async/await на замену @asyncio.coroutine и yield from
# 4. Пример асинхронного скачивания файлов


# Event Loop:
#     coroutine > Task (Future)

import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())
    
    
# python3
# import asyncio
# @asyncio.corotine
# def a():
#    return 'ok'
# 
# import inspect
# inspect.isgeneratorfunction(a)
# g = a()
# next(g)
# def a():
#	num = 1
# 	while True:
#		print(num)
#		num += 1
# a()


# python3 original.py

