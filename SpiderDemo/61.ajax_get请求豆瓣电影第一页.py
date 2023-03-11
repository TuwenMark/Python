# ajax的get请求获取第一页数据并将json数据写入文件中（Ajax滚动分页请求的第一页）
import json
import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 请求对象的封装
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器发起请求
response = urllib.request.urlopen(request)

# 读取响应数据
content = response.read().decode('utf-8')

# print(json.loads(content))

open('douban.json', 'w', encoding='utf-8').write(content)
