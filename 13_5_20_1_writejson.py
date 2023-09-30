# -*- coding: utf-8 -*-
# Auther : jianlong
import json, os


def write_json(path, data):
    with open(path, 'w') as f:
        if isinstance(data, dict):
            f.write(json.dumps(data))
        else:
            pass
    return True


def read_json(path):
    with open(path, 'r') as f:
        data = f.readlines()
        ss = ''
        for x in data:
            line = x.strip()
            if line != '':
                print(line)
                ss += line
    return json.loads(ss)


data = {'name': '小郭 ',
        'age': 26}
# write_json('test.json', data)

result = read_json('test.json')
print('结果为', result)
