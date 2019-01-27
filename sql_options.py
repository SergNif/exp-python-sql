# -*- coding: utf-8 -*-
import scrapy
from operator import methodcaller
#import time
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from unidecode import unidecode


def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def title():
    i={}
    for x in range(0, 10):
        i={}
        i['list_options' + str(x)] = ''
        i['list_options_value' + str(x)] = ''
        return i


class WoolSpider(CrawlSpider):

    
    name = 'option'
    allowed_domains = ['terrakot-yarn.ru']
    start_urls = ['http://terrakot-yarn.ru']
    
    rules = (
        Rule(
            LinkExtractor(
                # allow = 'terrakot-yarn.ru'#r'terrakot-yarn.ru/',#allow=r'zhenskaya_odezhda/dzhinsy/',
                # deny=('pryazha')  #, 'COUNT', 'filter'),
            ),
            callback='parse_item',
            follow=True), )

    def parse_item(responsef, response):

        i = {}
        #        [option_value_id] от 306 [option_id] всегда 2  [image] адрес, где картинка catalog/Alize/1/691684503-cotton-gold-plus-multi-color.jpg  [sort_order] всегда 0 ноль  oc_option_value.csv
        #   [option_value_id] от 306 [language_id] строка с значением 1 и копия со значением 2 [option_id] всегда 2  [name]  название фактуры  oc_option_value_description.csv
# получается ищем  [image] адрес, где картинка catalog/Alize/1/691684503-cotton-gold-plus-multi-color.jpg
# [name]  название фактуры  
# для адреса картинки нужна категория пряжи
# 
# 
# 
# 
# 
# 
        #try:
        #    if bw > 305:
        #        pass
        #except:
        #    bw = 305
#
        print (type(i))

        # ищет на странице фразу "карта цветов", чтобы понять, что находимся на странице товара
        if len(
                response.xpath(
                    '//div[@id="center"]//h5[contains(text(),"Карта цветов")]'
                ).extract()) >= 1:

            #ur = response.url
            #dom = response.meta.get('download_slot')
            #i['sku'] = ur[ur.find(dom) + len(dom) + 1:ur.find(dom) + len(dom) +
            #              10:].replace('_', '-')
            #i['Link'] = str(response)[5:-1]

            #  категории
            categ_dx = unidecode(response.xpath('//div[@id="container"]//div[@id="center"]/p/a/text()').extract()[::-1][0])


        # номера цветов  картинки   list(map(lambda x: response.url[:23]+x, sd))
            link_img = response.xpath('//div[@id="center"]/table[@class="main"]//tr/td[@class="items_div"]/img[re:match(@src,"jpg|png")]/@src').extract()  # список картинок
            name_img = response.xpath('//div[@id="center"]/table[@class="main"]//tr/td[@class="items_div"]//p[@class="text2"]/text()').extract()
            
            bw = 1
            for x in range(0,len(link_img)):
                
                i['option_value_id'] = bw
                i['option_id'] = 2
                i['image'] = 'catalog/'+categ_dx + link_img[x]
                i['sort_order'] = 0

            return i


# if __name__ == '__main__':
#   main()

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
# response.xpath("//span[contains(@style,'background-color')]").extract_first().split('"')[1].split('#')[1]
#  z=' '.join(a.split()) убрать все \n \t  из a

# запускать из домашней папки test командой  scrapy runspider jeans2.py -o bnb55.csv -t csv --nolog
# --nolog это не выводить сообщения
# jeans2.py это имя этого файла
# bnb55.csv это имя файла, куда будет записываться скрап (импорт), можно задать любое имя
# --set CLOSESPIDER_ITEMCOUNT=50  ОГРАНИЧЕНИЕ количества запросов
# scrapy runspider wool.py -o wool55.csv -t csv --set CLOSESPIDER_ITEMCOUNT=50 --nolog

# scrapy shell 'https://www.kupi-jeans.ru/zhenskaya_odezhda/dzhinsy/uteplennye_bryuki_dzhinsovye/dzhinsy_zhenskie_uteplennye_miss_bon_mb_702/' --nolog
# запускать оболочку scrapy  для какой-то страницы. тут можно запускать всякие запросы и смотреть что приходит в ответ с этой страницы

# Брюки джинсовые
# Комбинезоны и сарафаны
# Куртки, пиджаки и жилетки
# Распродажа
# Утепленные брюки джинсовые
#Шорты, бриджи, капри
