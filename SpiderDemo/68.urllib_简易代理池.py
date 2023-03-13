# 请求的基本信息：url、请求头、请求参数
import random
import urllib.request

url = 'https://www.baidu.com/s?wd=ip'
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 通过代理模拟浏览器向服务器发起请求
# 创建随机线程池
proxy_pool = [
	{'http': '111.184.226.3:8088'},
	{'http': '211.151.59.251:80'}
]
proxy = random.choice(proxy_pool)
print(proxy)
# （1）获取handler
handler = urllib.request.ProxyHandler()
# （2）获取opener
opener = urllib.request.build_opener(handler)
# （3）调用open方法，发起请求
response = opener.open(request)

# 获取响应数据
content = response.read().decode('utf-8')

# 保存
with open('daili.html', 'w', encoding='utf-8') as fp:
	fp.write(content)
	fp.close()
