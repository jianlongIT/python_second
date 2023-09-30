# -*- coding: utf-8 -*-
# Auther : jianlong
from concurrent.futures import ThreadPoolExecutor
import threading
import random

# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)  # 定义两个线程


def task(i):
    sleep_seconds = random.randint(1, 3)  # 随机睡眠时间
    print('线程名称：%s，参数：%s，睡眠时间：%s' % (threading.current_thread().name, i, sleep_seconds))


for i in range(10):  # 创建十个任务
    future1 = pool.submit(task, i)
