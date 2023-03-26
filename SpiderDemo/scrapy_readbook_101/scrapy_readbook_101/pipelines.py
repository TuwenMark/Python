# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyReadbook101Pipeline:

    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()

from scrapy.utils.project import get_project_settings
import pymysql

# 数据入库
class MysqlPipeline:
    # 获取配置，建立连接
    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        self.connect()

    def connect(self):
        # 获取数据库连接
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.name,
                                  charset=self.charset)
        # 获取执行数据库操作的对象
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 构建sql语句
        sql = 'insert into spider01(name, src) values ("{}", "{}")'.format(item['name'], item['src'])
        # 执行sql
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭连接
        self.conn.close()
        self.cursor.close()