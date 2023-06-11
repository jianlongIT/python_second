# -*- coding: utf-8 -*-
# Auther : jianlong
from functools import reduce
import json

data = filter(lambda x: x % 2 == 0, list(range(0, 51)))
print(list(data))

list_1 = map(lambda x: str(x).zfill(2), [1, 2, 3, 4])

print(list(list_1))

list_3 = map(lambda x: pow(x, 5), range(2, 13, 2))
print(tuple(list_3))

list_4 = reduce(lambda x, y: x * y, range(1, 21))
print(list_4)


