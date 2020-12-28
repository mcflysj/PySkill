"""
调用浏览器并打开指定网页
"""
import sys
import webbrowser


sys.path.append("libs")

url = 'http://www.baidu.com'
webbrowser.open(url)
