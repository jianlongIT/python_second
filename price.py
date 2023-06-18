# -*- coding: utf-8 -*-
# Auther : jianlong
import random
import threading

lists = list(range(1, 21))
lock = threading.Lock()


def get_price(i):
    lock.acquire()
    if 1 not in lists and 2 not in lists and 3 not in lists:
        print('抽奖结束了')
    result = random.choice(lists)
    lists.remove(result)
    if result == 1:
        print('手机号码为%s的用户抽中一等奖：手机，价值3999元' % i)
    elif result == 2:
        print('手机号码为%s的用户抽中二等奖：平板电脑，价值1999元' % i)
    elif result == 3:
        print('手机号码为%s的用户抽中三等奖：加湿器，价值198元' % i)
    lock.release()


if __name__ == '__main__':
    for i in range(1, 21):
        thr = threading.Thread(target=get_price, args=(random.randint(13000000000, 18000000000),))
        thr.start()
