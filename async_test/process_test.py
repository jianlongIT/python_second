# -*- coding: utf-8 -*-
# Auther : jianlong
import os
import time
import multiprocessing


def work_a():
    for i in range(0, 10):
        if i == 8:
            time.sleep(5)
        else:
            time.sleep(1)
        print(str(i) + 'name is a' + str(os.getpid()))


def work_b():
    for i in range(0, 10):
        time.sleep(1)
        print(str(i) + 'name is b' + str(os.getpid()))


if __name__ == '__main__':
    start = time.time()
    a_p = multiprocessing.Process(target=work_a)
    a_p.start()
    b_p = multiprocessing.Process(target=work_b)
    b_p.start()
    # b_p.join()
    a_p.join()
    end = time.time()
    print(end - start)
