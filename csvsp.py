import scrapy


class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()


from scrapy.spiders import CSVFeedSpider
from myproject.items import TestItem


class MySpider(CSVFeedSpider):
    name = 'example.com'
    allowed_domains = ['http://kupi-jeans.ru/']
    start_urls = ['http://kupi-jeans.ru/']
    delimiter = ';'
    quotechar = "'"
    headers = ['id', 'name', 'description']

    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row!: %r', row)

        item = TestItem()
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item