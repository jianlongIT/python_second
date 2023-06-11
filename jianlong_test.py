# -*- coding: utf-8 -*-
# Auther : jianlong
import yaml
import log_color
from ColorInfo import ColorLogger


class Jianlong(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b


jianlong = Jianlong('name', 27)
print(getattr(jianlong, 'a'))
setattr(jianlong, 'sex', 'man')
print(getattr(jianlong, 'sex'))
print(vars(jianlong))
print(hasattr(jianlong, 'sex'))
log = ColorLogger()
log.info(str(vars(jianlong)))

ss = ['1', '2', '3,4', 4, 5]
for i in enumerate(ss):
    print(i)
