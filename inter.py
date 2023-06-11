# -*- coding: utf-8 -*-
# Auther : jianlong
list1 = [{'name': 'jianlong', 'age': 27}, {'name': 'xiaoguo', 'age': 26}, {'name': 'xiaoguo2', 'age': 26}]
iters = iter(list1)
result = next(iters)
result2 = next(iters)
print(result)
print(result2)


def test():
    for i in list1:
        yield i


test_result = test()
t1 = next(test_result)
t2 = next(test_result)
print(t1, t2)

res = (i['name'] for i in list1)
print(next(res))
print(next(res))
print(next(res))

res4 = filter(lambda x: x['name'] == 'jianlong', list1)

print('res4', list(res4))
