# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pip._internal.cli.cmdoptions
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import urllib.request

class ScrapyDangdang095Pipeline:
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item) + ',')
        return item

    def close_spider(self, spider):
        self.fp.close()

# 多管道下载数据
class ScrapyDownloadPipeline:
    def process_item(self, item, spider):
        url = item.get('src')
        filename = './book_images/' + item.get('name') + '.jpg'
        # print(url, filename)
        urllib.request.urlretrieve(url= url, filename= filename)
        return item
