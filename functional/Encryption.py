"""
    多种加解密方法
"""


class Encryption:

    def __init__(self):
        self.count = 16

    def chr_all(self):
        # 常用字符串为32-->126
        for i in range(31, 128):
            print(str(i) + '-->' + chr(i))

    # 方法一：ord()函数就是用来返回单个字符的ASCII值（0-255）或者unicode数值，chr()函数返回字符
    def ord_encrypt(self, org_str):
        ord1 = ord('z')  # 122
        ord2 = ord('A')  # 65
        ord3 = ord(' ')  # 32
        ord4 = ord('1')  #
        chr1 = chr(54)
        # print(type(ord1),ord1,ord2,ord3,ord4)
        # print(type(chr1),chr1)

        secret_str = ''
        for st in org_str:
            if st.isspace():  # 判断输入的数据中是否有空格
                secret_str += str(ord(st))
            elif st.isalpha():  # 判断输入的数据是否为字母
                secret_str += str(ord(st) - 30)  # 35~96
            else:
                secret_str += str(ord(st) - 20)  #
        print('加密后的字符串为：', secret_str)
        return secret_str

    def chr_decrypt(self, secret_str):
        norm_str = ''
        for i in range(0, len(secret_str), 2):
            norm_info = secret_str[i:i + 2]
            if norm_info < '65':
                norm_str += str(chr(int(norm_info)))
            else:
                norm_str += str(chr(int(norm_info) + 30))
        print('解密后的字符串为：', norm_str)


if __name__ == '__main__':
    ways = Encryption()
    # chr_all()
    org_str = 'copera'
    print('原始的字符串数据：', org_str)
    secret_str = ways.ord_encrypt(org_str)
    ways.chr_decrypt(secret_str)
