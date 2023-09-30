# -*- coding: utf-8 -*-
# Auther : jianlong

import glob
import os, shutil


def update_name(path):
    result = glob.glob(path)
    for index, data in enumerate(result):
        if os.path.isdir(data):
            _path = os.path.join(data, "*")
            update_name(_path)
        else:
            path_list = os.path.split(data)
            path_name = path_list[-1]
            new_name = '%s_%s' % (index, path_name)
            new_data = os.path.join(path_list[0], new_name)
            shutil.move(data, new_data)

 
target = os.getcwd()
update_name(target+"/*")
