"""
    日常实用的技巧
"""


# 重复元素判定
def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]
all_unique(x)  # False
all_unique(y)  # True

# 字符元素组成判定(检查两个字符串的组成元素是不是一样的)
from collections import Counter


def anagram(first, second):
    return Counter(first) == Counter(second)


anagram("abcd3", "3acdb")  # True

# 内存占用
import sys

variable = 30
print(sys.getsizeof(variable))  # 24


# 字节占用
def byte_size(string):
    return (len(string.encode('utf-8')))


byte_size('😀')  # 4
byte_size('Hello World')  # 11

# 分块(给定具体的大小，定义一个函数以按照这个大小切割列表)
from math import ceil


def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))


chunk([1, 2, 3, 4, 5], 2)
# [[1,2],[3,4],5]

# 元音统计
import re


def count_vowels(str):
    return len(len(re.findall(r'[aeiou]', str, re.IGNORECASE)))


count_vowels('foobar')  # 3
count_vowels('gym')  # 0


# 列表的差
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


difference([1, 2, 3], [1, 2, 4])  # [3]


# 检查重复项
def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x)  # True
has_duplicates(y)  # False


# 合并两个字典
def merge_two_dicts(a, b):
    c = a.copy()  # make a copy of a
    c.update(b)  # modify keys and values of a with the ones from b
    return c


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_two_dicts(a, b))


# {'y': 3, 'x': 1, 'z': 4}

# 将两个列表转化为字典
def to_dictionary(keys, values):
    return dict(zip(keys, values))


keys = ["a", "b", "c"]
values = [2, 3, 4]
print(to_dictionary(keys, values))
# {'a': 2, 'c': 4, 'b': 3}

# 执行时间
import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c)  # 3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)


# ('Time: ', 1.1205673217773438e-05)

# 展开列表
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


spread([1, 2, 3, [4, 5, 6], [7], 8, 9])  # [1,2,3,4,5,6,7,8,9]
