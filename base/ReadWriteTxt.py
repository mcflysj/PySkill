"""
文本文件读取与写入

Version: 0.1
Author: Mcfly_SJ
Date: 2020-12-24
"""

import time


def read():
    # 一次性读取整个文件内容
    with open('../data/textDemo.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('../data/textDemo.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('../data/textDemo.txt') as f:
        lines = f.readlines()
    print(lines)


def write():
    # open函数第二个参数为a时是追加内容，为w时是重写整个文件
    with open('../data/textDemo.txt', 'a') as f:
        f.write("月儿弯弯" + '\n')
    print('写入完成!')


if __name__ == '__main__':
    read()
    write()
