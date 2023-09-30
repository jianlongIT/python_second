# -*- coding: utf-8 -*-
import random

list1 = random.sample(range(1, 33), 6)
list1.append(random.randint(1, 16))
print(list(map(lambda x: str(x).zfill(2), list1)))
