from scrapy.item import Item, Field
from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem


class StackItem(Item):
    husnr = Field()
    pris = Field()
    by = Field()
    periode = Field()



class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["cofman.com"]
    start_urls = [
    "http://www.cofman.com/search.php?country=DK#areaid=100001&areatxt=Danmark&country=DK&zoom=6&startDate=2015-08-29&endDate=2015-09-05&fuzzy=false",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//*[@id="content"]/div[4]')

        for question in questions:
            item = StackItem()
            item['husnr'] = question.xpath(
            '//*[@id="resultListning"]/div/div/div[1]/a/small').extract()
            item['pris'] = question.xpath(
            '//*[@id="resultListning"]/div/div/div[5]/div/div[1]//*/span[@class="formatted_price"]').extract()
            item['by'] = question.xpath(
            '//*[@id="resultListning"]/div/div/div[1]/a/text()').extract()
            item['periode'] = question.xpath(
            '//*[@id="mapNavigation"]/table/tbody/tr/td[1]/div/text()').extract()
            yield item