import urllib.parse
import urllib.request

# 本节内容：urlencode()方法可以编码字典对象

# 获取URL
base_url = 'https://www.baidu.com/s?wd='

data = {
    'name': '周杰伦',
    'sex': '男'
}

url = base_url + urllib.parse.urlencode(data)

# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器请求
response = urllib.request.urlopen(request)

# 打印数据
print(response.read().decode('utf-8'))
