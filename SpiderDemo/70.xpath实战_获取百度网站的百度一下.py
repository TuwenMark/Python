import urllib.request

from lxml import etree

# 1. 获取网站源码
url = 'https://www.baidu.com/'
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 2. 解析
tree = etree.HTML(content)
result = tree.xpath('//input[@id="su"]/@value')[0]

# 3. 处理数据
print(result)