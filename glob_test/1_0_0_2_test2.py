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
        if os.path.isfile(data):
            name = os.path.split(data)[-1]
            is_byte = False
            if data.endswith(".zip"):
                is_byte = True
                with open(data, 'rb') as f:
                    _content = f.read()
            else:
                with open(data, 'r') as f:
                    _content = f.read()
            if is_byte:
                hash_content_obj = hashlib.md5(_content)
            else:
                hash_content_obj = hashlib.md5(_content.encode('utf-8'))
            hash_content = hash_content_obj.hexdigest()
            try:
                if name in data_all:
                    is_del = False
                    for k, v in data_all[name].items():
                        if hash_content == v:
                            print(data + '被删除')
                            os.remove(data)
                            is_del = True
                    if not is_del:
                        data_all[name][data] = hash_content
                else:
                    data_all[name] = {
                        data: hash_content
                    }
            except Exception as e:
                print('error is in ', data, e, data_all[name])


target = os.path.join("/Users/dongzhiqiao/Downloads/githubProject/python_second")
clear(target)
print(data_all)
