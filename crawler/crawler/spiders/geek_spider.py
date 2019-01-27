from scrapy.spiders import CrawSpider, Rule
from scrapy.linkextractors import linkExtractor
from scrapy.selector import Selector



class GeekSpider(Spider):
    name = 'geek_spider'

    start_url = ['https://geekbrains.ru/courses/']
    allowed_domains = ['geekbrains.ru']

    rules = {




    }