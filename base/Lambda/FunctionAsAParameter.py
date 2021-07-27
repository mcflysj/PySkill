"""
函数作为参数
"""


numbers = [2, 3, 1, 7, 9]
numbers1 = list(
    map(lambda x: x * 2 + 1, numbers))
# numbers1 is [5, 7, 3, 15, 19]

numbers2 = list(
    filter(lambda x: x % 3 == 0, numbers))
# numbers2 is [3, 9]

print(numbers1)
print(numbers2)


