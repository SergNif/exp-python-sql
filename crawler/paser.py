#rom urllib.request import urlopen
#rom urllib.parse import urljoin
#rom lxml.html import fromstring

#RL = 'http://proglive.ru/courses'
#TEM_PATH = 'our-courses_list.our-courses_item'

#ef parse_courses():
	#f = urlopen(URL)
	#print(f)
	#f.read().f.read.decode('utf-8')
#
#
#
#
#
#
#
#ef #main():
	#parse_courses()
#
#f _#_name__ == '__main__':
	#main()
from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


class Airbnb(Item):
	size = Field()
	price = Field()
	name_text = Field()
	img = Field()
	add_img = Field()
	blok_item = Field()


class AirbnbCrawler(CrawlSpider):
	name = 'MiPrimerCrawler'
	start_urls = ['https://www.kupi-jeans.ru/zhenskaya_odezhda/dzhinsy/']
	allowed_domains = ['kupi-jeans.ru']

	rules = (
		Rule((LinkExtractor(allow =r'zhenskaya_odezhda`))),
		#Rule(LinkExtractor(allow=r''))

		)

	def parse_items(self, response):
		item=ItemLoader(AirbnbItem(), response)
		item.add_xpath('size','/html/body/div[3]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/ul/text()')
		item.add_xpath('price','/html/body/div[3]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[3]/span/text()')
		item.add_xpath('name_text','/html/body/div[3]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/text()')
		item.add_xpath('img','/html/body/div[3]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[1]/span/text()')
		item.add_xpath('add_img','/html/body/div[3]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/text()')
		item.add_xpath('blok_item','//*[@id="zoom"]/text()')

		yeld item.load_item()

