# -*- coding: utf-8 -*-
# Auther : jianlong
import re

str1 = 'jianlong@qq.com'
list = (re.findall('\w*', str1))
print(list)

str2 = 'I don\'t want to be your entire world, just the best thing in it, I want to say "$%^&*@#~!".'
str3 = '12i3 love 34you3 not 56because of 7who3 119 df44'
lis2 = re.findall('["]\W+["]', str2)
print(lis2[0])

lis3 = re.findall('\d+\w+\d+', str3)
print(lis3)

lis4 = re.findall('I .*(I wan.*say)', str2)
print(lis4[0])

email1 = 'lianflower@163.com'
email2 = '11123433@qq.com'
email3 = 'xinlang@sina.com'
print(re.findall('(.*)@.*\..*', email1))
print(re.search('.*@(.*)\..*', email1).group(1))
print(re.search('.*@(.*)\..*', email2).group(1))
print(re.search('.*@(.*)\..*', email3).group(1))

str_data = 'hello world'
print(re.split('o\Ww', str_data))

print('findall----', re.findall('fl(.*)', email1))
print('match----', re.match('.*fl(.*)', email1))
print('split----', re.split('fl(.*)', email1))
print('search----', re.search('fl(.*)', email1).groups())

ksf = '康师傅, 康帅傅, 康师傅, 康帅傅, 康帅傅, 康师傅, 康帅傅, 康师傅, 康帅傅, 康师傅';
print(len(re.findall('[^康师傅, ]', ksf)))

a = '康帅傅, 康师傅, 康帅傅, 康师傅, 康帅傅, 康帅傅, 康师傅, 康帅傅, 康师傅, 康帅傅, 康师傅'
str_test = a.replace('康师傅, ', '').replace(', 康师傅', '')
print(str_test)
a1 = re.findall('康师傅,*\s*', a)
print(a1)
print('小慕买到了{}包山寨方便面'.format(len(a1)))
