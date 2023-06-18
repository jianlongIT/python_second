# -*- coding: utf-8 -*-
# Auther : jianlong

import multiprocessing


def main_test(num):
    print('jianlong', num)


def run():
    pool = multiprocessing.Pool(10)
    pool.apply_async(func=main_test, args=('',))
    pool.close()
    pool.join()


if __name__ == '__main__':
    run()
