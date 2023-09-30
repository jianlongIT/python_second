# -*- coding: utf-8 -*-
# Auther : jianlong
import os
from shutil import copy, move, make_archive

path = os.getcwd()

copy('test1.txt', 'test1')

#move('move.txt', 'test1/move2')

make_archive('test1', 'zip', os.getcwd())
