"""
作为返回值的函数
"""


def make_sum_func():
    return lambda a, b: a + b


sumFunc = make_sum_func()
sumValue = sumFunc(5, 8)
# sumValue is 13

print(sumValue)
