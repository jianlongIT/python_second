# -*- coding: utf-8 -*-
# Auther : jianlong
import multiprocessing
import json
import time


class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        if not isinstance(message, str):
            self.q.put(json.dumps(message))
        else:
            self.q.put(message)

    def resv(self):
        while 1:
            try:
                q_str = self.q.get()
                result = json.loads(q_str)
            except Exception as e:
                print(e)
                result = q_str
            print('resv is {}'.format(result))


if __name__ == '__main__':
    q = multiprocessing.Queue()
    work = Work(q)
    send_t = multiprocessing.Process(target=work.send, args=({'name': 'jianlong'},))
    resv_t = multiprocessing.Process(target=work.resv)

    send_t.start()
    resv_t.start()

    send_t.join()
    resv_t.terminate()
