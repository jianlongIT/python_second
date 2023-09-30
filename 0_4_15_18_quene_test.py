# -*- coding: utf-8 -*-
# Auther : jianlong
import multiprocessing
import json
import threading
import time


def send(q):
    for message in range(1, 11):
        if not isinstance(message, str):
            result = json.dumps(message)
        else:
            result = message
        q.put(result)


def resv(q, name):
    while 1:
        try:
            res = json.loads(q.get())
            time.sleep(1)
        except Exception as e:
            print(e)
        print('第%s个蛋糕被%s吃掉了' % (res, name))


if __name__ == '__main__':
    quene = multiprocessing.Queue()
    mumu = threading.Thread(target=send, args=(quene,))
    xiaoming = threading.Thread(target=resv, args=(quene, '小明',))
    xiaohong = threading.Thread(target=resv, args=(quene, '小红',))
    anan = threading.Thread(target=resv, args=(quene, '安安',))
    mumu.start()
    xiaoming.start()
    xiaohong.start()
    anan.start()
