# -*- coding: utf-8 -*-
# Auther : jianlong
import yaml
import base64


def yaml_test(path):
    with open(path, 'r') as f:
        result = yaml.safe_load(f)
    return result


data = yaml_test('jianlong.yaml')
print(data)

ens = base64.encodebytes('hello world'.encode('utf-8'))
result1 = base64.decodebytes(ens)
print(result1.decode(encoding='UTF-8'))

ss = ['s', 'b', 'c']
for s, item in enumerate(ss):
    print(s, item)
