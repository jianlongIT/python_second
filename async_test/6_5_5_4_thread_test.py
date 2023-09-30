# -*- coding: utf-8 -*-
# Auther : jianlong
import random
import multiprocessing

sugers = list(range(100))


def getsuger(child_list, child_num):
    while len(sugers) > 0 and len(child_list) < 20:
        one_suger = random.choice(sugers)
        sugers.remove(one_suger)
        child_list.append(one_suger)
    print('第 %s 个孩子分到的糖果是 %s ' % (child_num, child_list))


if __name__ == '__main__':
    child = []
    pool = multiprocessing.Pool(5)
    for i in range(1, 6):
        pool.apply_async(func=getsuger, args=(child, i,))
    pool.close()
    pool.join()
