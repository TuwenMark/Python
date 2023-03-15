# url: https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx
# __VIEWSTATE: qBFOo1YMWFyzxJuqvUsdQ0u2RSNqWV5CgFcLxTlrp4+onBoYuWK3lfN+9eMyLV6FFoSYOEBExa481k/Lf/52Pt08lQgqAE+cIisURUaRudxzVwu6n5Jy8SdReG8LommXfqoxrTLJtNyKR7ElJjDU/d270tY=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: m18698577021@163.com
# pwd: YH836788744
# code: 2732
# denglu: 登录

import requests
from bs4 import BeautifulSoup

# （1）访问前准备
index_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# （2）访问登录页面，获取网页源码
response = requests.get(url=index_url, headers=headers)
content = response.text

# （3）从源码中定位获取__VIEWSTATE和__VIEWSTATEGENERATOR
soup = BeautifulSoup(content, 'lxml')
view_state = soup.select('#__VIEWSTATE')[0].get('value')
view_state_gen = soup.select('#__VIEWSTATEGENERATOR')[0].get('value')

# （4）定位验证码地址，下载验证码图片
code_prefix = 'https://so.gushiwen.cn'
code_suffix = soup.select('#imgCode')[0].get('src')
code_url = code_prefix + code_suffix
session = requests.session()
code_image = session.get(code_url).content
with open('code.png', 'wb') as fp:
	fp.write(code_image)
	fp.close()

# （5）登录请求
code = input('请输入验证码：')

login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
headers={
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
data = {
	'__VIEWSTATE': view_state,
	'__VIEWSTATEGENERATOR': view_state_gen,
	'from': 'http://so.gushiwen.cn/user/collect.aspx',
	'email': 'm18698577021@163.com',
	'pwd': 'YH836788744',
	'code': code,
	'denglu': '登录'
}

response = session.post(url=login_url, data=data, headers=headers)
content = response.text
with open('login.html', 'w', encoding='utf-8') as fp:
	fp.write(content)
	fp.close()
