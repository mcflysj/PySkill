"""
获取城市温度信息
知识点：熟悉可迭代对象及迭代器
"""
from collections.abc import Iterable, Iterator
import requests


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self, city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        # 使用元组的形式返回结果，只取接口调用结果中的部分信息
        return city, data['high'], data['low']


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def show(w):
    for x in w:
        print(x)

# 迭代器是一次性消费的，而可迭代对象可重复使用
w = WeatherIterable(['北京', '上海', '广州', '深圳', '海口', '三亚'])
show(w)
