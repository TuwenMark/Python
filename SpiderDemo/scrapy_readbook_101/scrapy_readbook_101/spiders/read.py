import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook_101.items import ScrapyReadbook101Item

class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["http://www.dushu.com//book/1158_1.html"]

    # allow：链接提取规则
    # callback：执行的提取逻辑
    # follow：是否跟进提取，即当页数不确定时，是否越过当前页面看到的页数向下提取
    rules = (Rule(LinkExtractor(allow=r"/book/1158_\d+\.html"),
                                callback="parse_item",
                                follow=True),)

    def parse_item(self, response):
        book_list = response.xpath('//div[@class="bookslist"]//img')
        for book in book_list:
            name = book.xpath('./@alt').extract_first()
            src = book.xpath('./@src').extract_first()
            book = ScrapyReadbook101Item(name=name, src=src)
            yield book
