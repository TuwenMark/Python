import urllib.request

url = 'https://weibo.cn/3848252545/info?rand=2802&p=r'

headers = {
	'cookie': 'SCF=An1attW9kv9LEogUNmV_0ehoXKF4YVelbCZeih7tmbi5JYbcJs-0nBSM_dNCPsPky5naXqCH6s7CbskG7UxavoU.; SUB=_2A25JCNS6DeRhGeVG71oT9SzJzzmIHXVq8vzyrDV6PUNbktCOLRLckW1NT7wzB458CXEsyjt66UiTsbNFly63sjRn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWa-jxWiHnOmU-k9OjpHW3e5JpX5KMhUgL.FoeRShnESKzfSh-2dJLoIESWCCHhebHFSEH8SCHFSEHWSEH8SC-RSC-RBbH8SC-RBC-4Bntt; SSOLoginState=1678550250; ALF=1681142250; _T_WM=6636fefc27762cbe91b5e9c03d561f89',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器发起请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

# 将数据写入文件
with open('weibo.html', 'w', encoding='utf-8') as fp:
	fp.write(content)
	fp.close()
