# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JeansSpider(CrawlSpider):
    name = 'jeans'
    allowed_domains = ['kupi-jeans.ru']
    start_urls = ['http://kupi-jeans.ru/']

    rules = (Rule(
        LinkExtractor(
            allow=r'zhenskaya_odezhda/dzhinsy/',
            deny=('PAGEN', 'COUNT', 'filter'),
        ),
        callback='parse_item',
        follow=True), )

    def parse_item(responsef, response):

        # if len(response.xpath('//div[@class="descr title-descr"]/h1/text()').extract_first()) > 0:

        i = {}
        i['name'] = response.xpath(
            '//div[@class="descr title-descr"]/h1/text()').extract_first()
        i['price'] = response.xpath(
            '//span[@class="new-price"]/text()').extract_first()
        i['img'] = response.xpath(
            '//div[@class="image"]/a/@href').extract_first()
        i['add_img'] = response.xpath(
            "//div[@class='catalog_object_thumbs']/*/img/@src").extract()
        i['categor_list'] = response.xpath(
            "//div[@class='bx-breadcrumb']/*/a[@title]/span/text()").extract()
        i['proizvodit'] = response.xpath(
            "//div[@class='new-info']/p[@class='new-manifacture']/text()").extract()
        i['country_proizvodit'] = response.xpath(
            "//div[@class='new-info']/p[@class='new-manifacture']/span/text()").extract()
        i['categor_list'] = response.xpath(
            "//div[@class='bx-breadcrumb']/*/a[@title]/span/text()").extract()
        i['artikul'] = response.xpath(
            "//div[@class='new-info']/p[@class='new-article']/text()").extract()
        i['size'] = response.xpath(
            "//ul[@class='parameters clearfix']/*/a[not(re:match(@class,'[with]'))]/text()").extract()
        #try:
        #    i['color'] = response.xpath(
        #        "//ul[@class='parameters clearfix']/*/a[re:match(@class,'[with]')]/span/@style").extract_first().split('#')[1]
        try:
            xx = response.xpath("//p[text()='О ТОВАРЕ']/following-sibling::div/text()").extract()
            f=' '.join(xx)
            i['title'] = ' '.join(f.split())
        except:
            pass

        #i['tablesize'] = response.xpath("//table[@class='sizetable']").extract()
        return i
# i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
# i['name'] = response.xpath('//div[@id="name"]').extract()
# i['description'] = response.xpath('//div[@id="description"]').extract()


# response.xpath("//a[re:match(@href,'zhen[\w\s]')]").extract()
# response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
# response.xpath("//ul[@class='parameters clearfix']/*/a/@data-models").extract() data-model
# response.xpath("//ul[@class='parameters clearfix']/*/a[not(re:match(@class,'[with]'))]/text()").extract()
 #response.xpath("//div[@class='descr item_description']").extract()

# response.xpath("///div[4]/div[4]/div[2]/div/div[2]/div[1]/div/following-sibling::*/node()").extract()[3]  #это пример, что такие xpath тоже работают
#sel.xpath("//p[text()='О ТОВАРЕ']/following-sibling::div/text()").extract()
#  z=' '.join(a.split()) убрать все \n \t  из a


# запускать из домашней папки test командой  scrapy runspider jeans2.py -o bnb55.csv -t csv --nolog
# --nolog это не выводить сообщения
# jeans2.py это имя этого файла
# bnb55.csv это имя файла, куда будет записываться скрап (импорт), можно задать любое имя
