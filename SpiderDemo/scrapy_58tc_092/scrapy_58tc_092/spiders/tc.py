import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["nj.58.com"]
    start_urls = ["https://nj.58.com/"]

    def parse(self, response):
        xpath = response.xpath('//li/a[@class="navWit"]/text()')[0]
        print('=====================')
        print(xpath)
        print(xpath.extract())