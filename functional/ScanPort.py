"""
    扫描指定ip的端口
"""
import _thread
import socket
import time

socket.setdefaulttimeout(3)


def socket_port(ip, port):
    try:
        if port >= 65535:
            print(u"端口扫描结束")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            print("used : {}:{}\n".format(ip, port))
            lock.release()
    except:
        print(u"扫描port异常")


def ip_scan(ip):
    try:
        print(u"开始扫描:{}\n".format(ip))
        start_time = time.time()
        for i in range(0, 65535):
            try:
                _thread.start_new_thread(socket_port, (ip, int(i)))
            except:
                print(u"扫描ip异常")
        end_time = time.time()
        print(u"共用时间：{}".format(end_time - start_time))
    except:
        print(u"扫描ip异常")


if __name__ == '__main__':
    url = str(input('请输入ip:\n'))
    lock = _thread.allocate_lock()
    ip_scan(url)