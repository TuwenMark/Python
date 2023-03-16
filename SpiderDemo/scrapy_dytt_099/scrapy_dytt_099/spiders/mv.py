import scrapy
from scrapy_dytt_099.items import ScrapyDytt099Item


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["www.ygdy8.net"]
    start_urls = ["https://www.ygdy8.net/html/gndy/china/index.html"]

    def parse(self, response):
        name_list = response.xpath('//div[@class="co_content8"]//table//a[2]/text()')
        src_list = response.xpath('//div[@class="co_content8"]//table//a[2]/@href')
        for i in range(len(name_list)):
            self.name = name_list[i].extract()
            href = src_list[i].extract()
            url = 'https://www.ygdy8.net' + href
            yield scrapy.Request(url=url, callback=self.parse_image, meta={'name': self.name})

    def parse_image(self, response):
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']
        movie = ScrapyDytt099Item(src=src, name = name)
        yield movie
