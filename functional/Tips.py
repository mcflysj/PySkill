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
