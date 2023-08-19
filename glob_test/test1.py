# -*- coding: utf-8 -*-
# Auther : jianlong

import os
from glob import glob

target = os.getcwd()


def get_file(path):
    result = glob(os.path.join(path, '*'))
    for data in result:
        if os.path.isdir(data):
            get_file(data)
        if os.path.isfile(data):
            print(data)


def get_file_test(path, search_text):
    result = glob(os.path.join(path, '*'))
    for data in result:
        if os.path.isdir(data):
            get_file_test(data, search_text)
        if os.path.isfile(data) and not data.endswith(".zip"):
            with open(data, 'r') as f:
                content = f.read()
                if search_text in content:
                    print(data)


# get_file('/Users/dongzhiqiao/Downloads/githubProject/python_second')
# get_file_test('/Users/dongzhiqiao/Downloads/githubProject/python_second', 'admin')
