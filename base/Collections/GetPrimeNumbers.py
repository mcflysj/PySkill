"""
获取两个数间的素数
"""
from collections.abc import Iterable


class PrimeNumbers(Iterable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a, self.b + 1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        # 排除掉0和1
        return False if k < 2 else all(map(lambda x: k % x, range(2, k)))


pn = PrimeNumbers(1, 50)
for n in pn:
    print(n)
