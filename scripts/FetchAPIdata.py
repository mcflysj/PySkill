# 需要从数据库中获取 API 数据或需要向服务器发送 API 请求。
# pip install urllib3
import urllib3
# Fetch API data
url = "https://api.github.com/users/psf/repos"
http = urllib3.PoolManager()
response = http.request('GET', url)
print(response.status)
print(response.data)
# Post API data
url = "https://httpbin.org/post"
http = urllib3.PoolManager()
response = http.request('POST', url, fields={'hello': 'world'})
print(response.status)