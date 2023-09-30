# -*- coding: utf-8 -*-
# Auther : jianlong
import os
from shutil import copy, move, make_archive, unpack_archive, copytree

path = os.getcwd()

copy('test1.txt', 'test1')

# move('move.txt', 'test1/move2')

# make_archive('test1', 'zip', os.getcwd())
# unpack_archive('test1.zip', 'unzip')

# make_archive('test1.txt', 'zip', os.getcwd())
# unpack_archive('test1.txt.zip', os.path.join(os.getcwd(), 'unzip2'))
# copytree('unzip', 'unzip2')
move('test1.zip', 'test1/test6.zip')
