# 本节内容：找到接口的规律，请求前10页数据
import urllib.parse
import urllib.request


# 1. 请求对象的定制
# 2. 模拟浏览器发送请求，获取数据
# 3. 数据下载

def create_request(page):
	origin_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action='
	origin_data = {
		'start': page - 1,
		'limit': 20,
	}
	data = urllib.parse.urlencode(origin_data)
	url = origin_url + data
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
	}
	request = urllib.request.Request(url=url, headers=headers)
	return request


def get_content(request):
	response = urllib.request.urlopen(request)
	content = response.read().decode('utf-8')
	return content


def download(page, content):
	with open('douban' + str(page) + '.json', 'w', encoding='utf-8') as fp:
		fp.write(content)


if __name__ == '__main__':
	start_page = int(input("请输入起始页码："))
	end_page = int(input("请输入结束页码："))
	for page in range(start_page, end_page + 1):
		# 请求对象的定制
		request = create_request(page)
		content = get_content(request)
		download(page, content)
