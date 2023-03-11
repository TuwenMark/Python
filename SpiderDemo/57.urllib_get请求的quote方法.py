import urllib.request
import urllib.parse

# 本节内容：quote()方法可以编码字符串

base_url = 'https://www.baidu.com/s?wd='

# UA
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = base_url + urllib.parse.quote('周杰伦')

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器请求
response = urllib.request.urlopen(request)

# 读取响应内容
print(response.read().decode('utf-8'))
