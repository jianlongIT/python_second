# -*- coding: utf-8 -*-
# Auther : jianlong
import os

print(os.getcwd() + '/second.test')
with open(os.getcwd() + '/second.test', 'r') as f:
# f.write('hello jianlong')
# f.seek(0)
    result = f.read()
    print(result)
    print('-------')
    f.seek(0)
    results = f.readlines()
    print(results)
    print(f.name)
print(f.closed)
