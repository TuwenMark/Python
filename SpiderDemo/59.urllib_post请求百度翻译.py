import json
import urllib.request
import urllib.parse

# 本节内容：① post请求的参数放在请求对象定制中；② post请求参数需要编码之后再encode()

# 基础的URL
url = 'https://fanyi.baidu.com/sug'

# 请求body体
origin_data = {
    'kw': 'hello'
}
data = urllib.parse.urlencode(origin_data).encode('utf-8')


# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器请求
response = urllib.request.urlopen(request)

# 读取数据(json数据)
content = response.read().decode('utf-8')
print(content)

# 反序列化至json对象
print(json.loads(content))
