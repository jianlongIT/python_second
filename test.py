# -*- coding: utf-8 -*-
# Auther : jianlong
import json

set1 = ["1", "2", "4", "1"]
print(set1, type(set1))
set1_json = json.dumps(set1)
print(set1_json, type(set1_json))

str_set1 = json.dumps(set1)
print(str_set1)
str_obj = json.loads(str_set1)
print(str_obj, type(str_obj))

str3 = 's'
str_1 = json.dumps(str3)
str4 = json.loads(str_1)
print(str4)

set2 = set([1, 2, 3, 4])
print(set2)
