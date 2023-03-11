# 本节内容：① Ajax的post请求；② 寻找接口规律
import urllib.parse
import urllib.request


def create_request(page):
	url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
	origin_data = {
		'cname': '南京',
		'pid': '',
		'pageIndex': page,
		'pageSize': '10',
	}
	data = urllib.parse.urlencode(origin_data).encode('utf-8')
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
	}
	request = urllib.request.Request(url, data, headers)
	return request


def get_content(request):
	response = urllib.request.urlopen(request)
	content = response.read().decode('utf-8')
	return content


def download(page, content):
	with open("KFC" + str(page) + '.json', 'w', encoding='utf-8') as fp:
		fp.write(content)


if __name__ == '__main__':
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))
	# 请求对象的定制
	for page in range(start_page, end_page + 1):
		request = create_request(page)
		content = get_content(request)
		download(page, content)
