import urllib.request

url = 'http://www.baidu.com'

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器发起请求
# （1）获取handler对象
handler= urllib.request.HTTPHandler()
# （2）获取opener对象
opener = urllib.request.build_opener(handler)
# （3）调用open方法发起请求
response = opener.open(request)

# 获取响应数据
content = response.read().decode('utf-8')

# 将数据写入文件
with open('baidu.html', 'w', encoding='utf-8') as fp:
	fp.write(content)
	fp.close()
