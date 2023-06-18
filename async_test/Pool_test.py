# -*- coding: utf-8 -*-
# Auther : jianlong
import os
import multiprocessing
import random
import time


def test():
    print('jianlong test')


def main_test(num, arg_lock):
    arg_lock.acquire()
    print(num, os.getpid())
    test()
    time.sleep(1)
    arg_lock.release()
    return 'jianlong'


if __name__ == '__main__':
    print(isinstance('', str))
    print()

    results = []
    pool = multiprocessing.Pool(15)
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    for i in range(20):
        res = pool.apply_async(func=main_test, args=(i, lock))
        results.append(res)

    pool.close()
    pool.join()
    for s in results:
        print(s.get())
