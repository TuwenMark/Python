import urllib.request
from lxml import etree


def create_request(page):
	if (page == 1):
		url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian.html'
	else:
		url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian_' + str(page) + ".html"
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
	}
	request = urllib.request.Request(url=url, headers=headers)
	return request

def get_content(request):
	response = urllib.request.urlopen(request)
	content = response.read().decode('utf-8')
	return content

def download(content):
	tree = etree.HTML(content)
	name_list = tree.xpath('//div[@class="container"]//img/@alt')
	url_list = tree.xpath('//div[@class="container"]//img/@data-original')
	for i in range(len(name_list)):
		urllib.request.urlretrieve('https:' + url_list[i], './sexy_images/' + name_list[i] + '.jpg')


if __name__ == '__main__':
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))

	for page in range(start_page, end_page + 1):
		# 1. 请求对象的定制
		request = create_request(page)
		# 2. 获取网页源码
		content = get_content(request)
		# 3. 下载
		download(content)