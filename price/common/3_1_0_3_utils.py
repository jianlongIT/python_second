# -*- coding: utf-8 -*-
# Auther : jianlong
import os

from price.common import error
import time


def check(path):
    if not os.path.isfile(path):
        raise error.NotFileError()
    if not os.path.exists(path):
        raise error.NotPathError()
    if not path.endswith('.json'):
        raise error.FileFormatError()


def timestamp_to_string(timestamp):
    time_obj = time.localtime(timestamp)
    time_string = time.strftime("%Y-%m-%d %H:%M:%S", time_obj)
    return time_string
