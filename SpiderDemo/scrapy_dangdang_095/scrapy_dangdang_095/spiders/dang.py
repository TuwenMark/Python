import scrapy

from scrapy_dangdang_095.items import ScrapyDangdang095Item



class DangSpider(scrapy.Spider):
	name = "dang"
	allowed_domains = ["category.dangdang.com"]
	# 起始url
	start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]
	base_url = 'http://category.dangdang.com/pg'
	page_num = 1
	# http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html

	def parse(self, response):
		protocol = 'https:'
		# 元素定位
		li_list = response.xpath('//ul[@id="component_59"]/li')
		for li in li_list:
			# 图片懒加载，获取data-original的属性值
			src = li.xpath('.//img/@data-original').extract_first()
			if src == None:
				# 第一本书没有data-original懒加载属性，获取src属性值
				src = li.xpath('.//img/@src').extract_first()
			src = protocol + src
			name = li.xpath('.//img/@alt').extract_first()
			price = li.xpath('.//p[@class="price"]/span/text()').extract_first()
			book = ScrapyDangdang095Item(src=src, name=name, price=price)
			# 将数据传给pipeline处理
			yield book

		if self.page_num < 100:
			self.page_num += 1
			url = self.base_url + str(self.page_num) + '-cp01.01.02.00.00.00.html'
			yield scrapy.Request(url=url, callback=self.parse)

