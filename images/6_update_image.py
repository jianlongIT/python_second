# -*- coding: utf-8 -*-
# Auther : jianlong
import os, shutil, glob

path = os.getcwd()
result = glob.glob(os.path.join(path, "*"))
for index, data in enumerate(result):
    path_list = os.path.split(data)
    if not path_list[-1].endswith('py'):
        new_name = '%s_%s' % ('imooc_', str(index) + '.' + path_list[-1].split('.')[-1])
        new_data = os.path.join(path_list[0], new_name)
        shutil.move(data, new_data)
