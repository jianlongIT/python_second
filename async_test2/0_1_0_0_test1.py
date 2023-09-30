# -*- coding: utf-8 -*-
# Auther : jianlong
import asyncio
import time
import random


async def a():
    for i in range(10):
        print(i, 'a')
        await asyncio.sleep(random.randint(1, 4))
    return 'a function'


async def b():
    for i in range(10):
        print(i, 'b')
        await asyncio.sleep(random.randint(1, 4))
    return 'b function'


async def run_all():
    result = await asyncio.gather(a(), b())
    print(result)


if __name__ == '__main__':
    asyncio.run(run_all())
