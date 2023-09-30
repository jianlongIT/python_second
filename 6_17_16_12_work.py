# -*- coding: utf-8 -*-
# Auther : jianlong
import random


def test():
    while True:
        yours = input('请输入你的选择')
        computer = random.randint(0, 2)
        print('你的选择{}     机器的选择{}'.format(yours, computer))

        if yours == computer:
            print('平局')
        if (int(yours) + 1) % 3 == computer:
            print('你赢了')
        else:
            print('你输了')


test()
