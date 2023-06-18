# -*- coding: utf-8 -*-
# Auther : jianlong
# -*- coding: utf-8 -*-
# Auther : jianlong
import random
from concurrent.futures import ThreadPoolExecutor


def get_sugar(child_list, child_num):
    while len(sugars) > 0 and len(child_list) < 20:
        one_sugar = random.choice(sugars)
        sugars.remove(one_sugar)
        child_list.append(one_sugar)
    print('第 %s 个孩子分到的糖果是 %s \n' % (child_num, child_list))


pool = ThreadPoolExecutor(max_workers=5)
if __name__ == '__main__':
    sugars = list(range(100))
    for i in range(1, 6):
        child = []
        pool.submit(get_sugar, child, i)
