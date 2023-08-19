# -*- coding: utf-8 -*-
# Auther : jianlong
from glob import glob
import os, hashlib

data_all = {}


def clear(path):
    result = glob(os.path.join(path, '*'))
    for data in result:
        if os.path.isdir(data):
            clear(data)
        if os.path.isfile(data) and not data.endswith(".zip"):
            name = os.path.split(data)[-1]
            with open(data, 'r') as f:
                _content = f.read()
            try:
                if name in data_all:
                    is_del = False
                    for k, v in data_all[name].items():
                        if _content == v:
                            print(data + '被删除')
                            os.remove(data)
                            is_del = True
                    if not is_del:
                        data_all[name][data] = _content
                else:
                    data_all[name] = {
                        data: _content
                    }
            except Exception as e:
                print('error is in ', data, e, data_all[name])


target = os.path.join("/Users/dongzhiqiao/Downloads/githubProject/python_second")
clear(target)
print(data_all)
