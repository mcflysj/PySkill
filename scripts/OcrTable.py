
# encoding:utf-8

import requests
import base64

'''
表格文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/table"
# 二进制方式打开图片文件
f = open('IMG_29431.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.83c01e5bd4cbad96610d6b75bf7c6bf1.2592000.1687417718.282335-33890283'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())