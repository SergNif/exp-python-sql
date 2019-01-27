# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider


class ParsercsvSpider(CSVFeedSpider):
    name = 'parsercsv'
    allowed_domains = ['kupi-jeans.ru']
    start_urls = ['http://kupi-jeans.ru/feed.csv']
    headers = ['id', 'name', 'description', 'image_link']
    delimiter = '\t'

    # Do any adaptations you need here
    def adapt_response(self, response):
        return response

    def parse_row(self, response, row):
        i = {}
        i['url'] = row['url']
        i['name'] = row['name']
        i['description'] = row['description']
        return i
