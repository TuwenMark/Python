import scrapy


class CarhomeSpider(scrapy.Spider):
    name = "carhome"
    allowed_domains = ["car.autohome.com.cn"]
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        print('=========================')
        name_list = response.xpath('//div[@class="list-cont-main"]/div/a/text()')
        price_list = response.xpath('//div[@class="main-lever-right"]//span[@class="font-arial"]/text()')
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name, price)
