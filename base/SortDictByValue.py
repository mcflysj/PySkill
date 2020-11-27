"""
根据字典中值的大小, 对字典中的项排序
案例：按成绩从大到小将10名学生进行排序
使用3种方式:
方式1:使用列表解析方式将字典中的项转化为(值，键)元组，然后使用内置函数sorted
方式2:使用zip将字典中的项转化为(值，键)元组，然后使用内置函数sorted
方式3:直接指定sorted函数的key参数

Version: 0.1
Author: Mcfly_SJ
Date: 2020-11-28
"""
from random import randint

# 构建范例数据(字典结构，键为学生名，值为分数)
students = {s: randint(60, 100) for s in 'abcdefghij'}
print("初始学生信息：")
print(students)

# 方式1：使用列表解析方式将字典转化为元组，并颠倒键值顺序
tmpByList = [(v, k) for k, v in students.items()]
# 调用内置函数sorted，设置reverse为True是将结果进行降序排列
retByList = sorted(tmpByList, reverse=True)

# 方式2:使用zip将字典中的项转化为(值，键)元组
tmpByZip = list(zip(students.values(), students.keys()))
retByZip = sorted(tmpByZip, reverse=True)

# 方式3:直接指定sorted函数的key参数，item[0]为姓名，item[1]为成绩
retByKey = sorted(students.items(), key=lambda item: item[1], reverse=True)

print("排序后的学生信息：")
print("方式1结果：%s" % retByList)
print("方式2结果：%s" % retByZip)
print("方式3结果：%s" % retByKey)

# 增加排名序号，名字为key，排名及成绩元组为value
ret = {k: (i, v) for i, (k, v) in enumerate(retByKey, 1)}
print("增加排名序号后的结果：")
print(ret)
