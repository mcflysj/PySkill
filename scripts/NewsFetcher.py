# 获取新闻文章
# pip install requests
import requests
ApiKey = "YOUR_API_KEY"
url = "https://api.worldnewsapi.com/search-news?text=hurricane&api-key={ApiKey}"
headers = {
  'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
print("News: ", response.json())