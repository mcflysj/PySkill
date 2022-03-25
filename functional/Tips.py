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
