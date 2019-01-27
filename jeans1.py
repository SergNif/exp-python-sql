# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JeansSpider(CrawlSpider):
    name = 'jeans'
    allowed_domains = ['kupi-jeans.ru']
    start_urls = ['http://kupi-jeans.ru/']

    rules = (
        Rule(LinkExtractor(allow=r'zhenskaya_odezhda/dzhinsy/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['domain_id'] = response.xpath('//div[@class="descr title-descr"]/h1/text()').extract_first()
        i['name'] = response.xpath('//span[@class="new-price"]/text()').extract_first()
        i['description'] = response.xpath('//div[@class="image"]/a/@href').extract_first()
 
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
