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
	allowed_domains = ['kupi-jeans.ru/zhenskaya_odezhda/dzhinsy/']

	rules = (
		Rule(LinkExtractor(allow =('/zhenskaya_odezhda')),callback='parse_items'),
		#Rule(LinkExtractor(allow=('bryuki')), callback='parse_items'),
		)

	def parse_items(self, response):
		item=ItemLoader(Airbnb(), response)
		item.add_xpath('size','/html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]text()')
		item.add_xpath('price','/html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[3]/span/text()')
		item.add_xpath('name_text','/html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/h1/text()')
		item.add_xpath('img','/html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[5]/a/img/text()')
		item.add_xpath('add_img','/html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[6]/a/img/text()')
		item.add_xpath('blok_item','/html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]/div[1]/div[1]/text()')
		yield item.load_item()

