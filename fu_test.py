# -*- coding: utf-8 -*-
# Auther : jianlong
import random

happy = [
    {"name": "富强福", "num": 0},
    {"name": "和谐福", "num": 0},
    {"name": "友善福", "num": 0},
    {"name": "爱国福", "num": 0},
    {"name": "敬业福", "num": 0}
]

while not all(list(map(lambda x: x["num"], happy))):
    start = input("按下<Enter>键集五福，迎新春")
    if isinstance(start, str):
        random.choice(happy)["num"] += 1
        print("当前拥有的福:")
        for kws in happy:
            print(kws["name"], ":", kws["num"], end="\t\t")
print("集齐五福了～\n")
exit(0)
