# -*- coding: utf-8 -*-
# Auther : jianlong
import gevent
import random

beans = list(range(1, 52))


def a():
    a_list = []
    print('a function')
    while len(beans) > 0:
        num = random.choice(beans)
        beans.remove(num)
        a_list.append(num)
        gevent.sleep(random.random())
    if len(beans) == 0:
        return a_list


def b():
    b_list = []
    print('b function')
    while len(beans) > 0:
        num = random.choice(beans)
        beans.remove(num)
        b_list.append(num)
        gevent.sleep(random.random())
    if len(beans) == 0:
        return b_list


if __name__ == '__main__':
    g_a = gevent.spawn(a)
    g_b = gevent.spawn(b)

    result = gevent.joinall([g_a, g_b])
    print(result[0].value, '\n', result[1].value)
