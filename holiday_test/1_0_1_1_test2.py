# -*- coding: utf-8 -*-
# Auther : jianlong
import re

lists = ['131,0000,0001',
         '131,0000,0002',
         '131,0000,0003',
         '131,0000,0004',
         '131,0000,0005']
print(list(map(lambda x: ''.join(x.split(',')), lists)))

s = '100'  # 1-100内的任意数字
ret = re.match('(100|[1-9]\n{0,1})$', s)
print(ret.group())

sss = 'my name is jianlong'
print(re.findall(r'\w+ng\b', sss))

print(sss + '\b')

s = "我我...我我...我要..要要...要要...学学学...学学..Python...编编编..编程..程.程...程...程"
print('---', re.findall('\W+', s, re.A))
res = re.sub(r'\W+', '', s)
print(res)
ret = re.sub(r'(.)\1+', r'\1', res)
print(ret)

s2 = "我我...我我...我要..要要...要要...学学学...学学..Python...编编编..编程..程.程...程...程"
res = re.sub(r'\W+', '', s2)
print(res)

test2 = 'jjjiiiaaaalllooonnnggg'
print(re.sub(r'(\w)\1+', r'\1', test2))
