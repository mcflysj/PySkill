"""
在列表，字典，集合中根据条件筛选数据
案例1：去除列表中的负数
案例2：筛选出字典中值大于90的项
案例3：筛选出集合中能被3整除的元素
每种数据结构分别使用两种方式

Version: 0.1
Author: Mcfly_SJ
Date: 2020-11-27
"""

from random import randint

"""
案例1：去除列表中的负数
"""
# 构造列表随机数
listDemo = [randint(-10, 10) for _ in range(10)]
print("*** 列表范例数据： ***")
print(listDemo)
# 方式1：使用列表解析
listResult = [x for x in listDemo if x >= 0]
print("方式1(列表解析)处理结果：")
print(listResult)
# 方式2：使用内置函数filter
listResult = filter(lambda x: x >= 0, listDemo)
# 在python3中filter函数返回的是生成器对象，此处用list构造器便于显示结果
print("方式2(filter函数)处理结果：")
print(list(listResult))

"""
案例2：筛选出字典中值大于90的项
"""
# 构造字典随机数
dictDemo = {'num%d' % i: randint(80, 100) for i in range(1, 11)}
print("*** 字典范例数据： ***")
print(dictDemo)
# 方式1：使用字典解析
dictResult = {k: v for k, v in dictDemo.items() if v > 90}
print("方式1(字典解析)处理结果：")
print(dictResult)
# 方式2：使用内置函数filter
dictResult = filter(lambda item: item[1] > 90, dictDemo.items())
print("方式2(filter函数)处理结果：")
print(dict(dictResult))

"""
案例3：筛选出集合中能被3整除的元素
"""
# 构造集合随机数
setDemo = {randint(1, 20) for _ in range(10)}
print("*** 集合范例数据： ***")
print(setDemo)
# 方式1：使用集合解析
setResult = {x for x in setDemo if x % 3 == 0}
print("方式1(集合解析)处理结果：")
print(setResult)
# 方式2：使用内置函数filter
setResult = filter(lambda x: x % 3 == 0, setDemo)
print("方式2(filter函数)处理结果：")
print(set(setResult))
