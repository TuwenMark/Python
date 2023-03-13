import urllib.request

# 请求基本信息：url、请求头、请求参数
url = 'http://www.baidu.com/s?wd=ip'
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 通过代理访问服务器
proxies = {
	'http': '111.184.226.3:8088'
}
# （1）获取handler对象
handler = urllib.request.ProxyHandler(proxies=proxies)
# （2）获取opener对象
opener = urllib.request.build_opener(handler)
# （3）调用open方法
response = opener.open(request)

# 获取响应数据内容
content = response.read().decode('utf-8')

# 保存
with open('ip.html', 'w', encoding='utf-8') as fp:
	fp.write(content)
	fp.close()
