# -*- coding: utf-8 -*-
import scrapy
import time
import re
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
        name_dx = str(
            response.xpath('//div[@class="descr title-descr"]/h1/text()').
            extract_first())
        name_dx = name_dx.lstrip().rstrip()

        price_dx = int(
            re.findall(
                r'\b\d+\b',
                response.xpath('//span[@class="new-price"]/text()').
                extract_first())[0])

        if (name_dx == 'None') or (price_dx <= 100):  # len(name_dx) > 0:
            pass
        else:

            i = {}
            # response.xpath('//div[@class="descr title-descr"]/h1/text()').extract_first()
            i['name'] = name_dx
            price = price_dx
            i['price'] = price + 400
            i['price_z'] = price
            i['sku'] = 'ARK-' + str(response.xpath("//div[@class='new-info']/p[@class='new-article']/text()").extract()).strip('[]').split(':')[1].strip()[:-1]        
            size_dx = response.xpath("//ul[@class='parameters clearfix']/*/a[not(re:match(@class,'[with]'))]/text()").extract()
            i['size_nm'] = "Size"
            i['size'] = ';'.join(size_dx)
            xx = response.xpath("//p[text()='О ТОВАРЕ']/following-sibling::div/text()").extract()
            f = ' '.join(xx)
            i['title'] = ' '.join(f.split())
            i['quantity'] = 10
            a = str(response)[5:]
            i['Link'] = a[:len(a) - 1]

            #i['size'] = response.xpath("//ul[@class='parameters clearfix']/*/a[not(re:match(@class,'[with]'))]/text()").extract()
            #try:
            i['color_nm'] = 'Color'
            #color_dx = response.xpath("//span[contains(@style,'back')]/@style").extract_first().split('#')[1]
            i['color'] = response.xpath("//span[contains(@style,'back')]/@style").extract_first().split('#')[1]
            i['country_proizvodit'] = response.xpath(
                "//div[@class='new-info']/p[@class='new-manifacture']/span/text()"
            ).extract()
 
            #i['photo'] = 'https://www.kupi-jeans.ru' + response.xpath('//div[@class="image"]/a/@href').extract_first()add_photo_dx = response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
            #for y in range(1, 10):
            #    if len(add_photo_dx) > 0:
            #        break
            #    else:
            #        time.sleep(2)
            #        add_photo_dx = response.xpath(
            #            "//div[@class='catalog_object_thumbs']/*/img/@src"
            #        ).extract()
            #        #break
            resp_foto = response.xpath(
                "//div/*/a[re:match(@href,'upload.iblock.*jpg')]").extract()
            #результат запроса , опрашиваем каждый элемент a[0]... в цикле  , разбиваем на части  a[1].split('"')
            # , и получаем ссылку картинки a[1].split('"')[1] плюс имя домена
            for t, j in enumerate(resp_foto):  #for m in resp_foto:
                if str(t).strip() != '':
                    i['resp_foto' + str(t)] = 'https://www.kupi-jeans.ru' + j.split('"')[1]
            for x in range(15, len(resp_foto), -1):
                i['resp_foto' + str(x)] = ''            
            #add_photo_dx = add_photo_dx[:len(add_photo_dx)]
            #for x in range(12, len(add_photo_dx), -1):
            #    i['add_photo_dx' + str(x)] = ''
            #for t, j in enumerate(add_photo_dx):
            #    i['add_photo_dx' + str(t)] = 'https://www.kupi-jeans.ru' + j  #add_photo_dx #'https://www.kupi-jeans.ru'+response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
            #    #add_photo_dx[t] = 'https://www.kupi-jeans.ru'+ add_photo_dx[t]
            #    #i['add_photo'+str(t)] = 'https://www.kupi-jeans.ru'+j #add_photo_dx #'https://www.kupi-jeans.ru'+response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()

            categ_dx = response.xpath(
                "//div[@class='bx-breadcrumb']/*/a[@title]/span/text()"
            ).extract()[1:]
            categ_dx = categ_dx[:len(categ_dx)]
            for x in range(10, len(categ_dx), -1):
                i['categor_list' + str(x)] = ''
            for g, c in enumerate(categ_dx):
                i['categor_list' + str(g)] = c


            i['quantity opc'] = '10;10;10;10;10;10;10;10;10'
            
            try:
                z=int(response.xpath('//div[@class="price"]/span[@class="old-price"]/text()').extract_first()[:-4].strip()) + 400
            except :
                z=''
            i['old-price'] = z #int(response.xpath('//div[@class="price"]/span[@class="old-price"]/text()').extract_first()[:-4].strip()) + 400
            


            #int(response.xpath('//span[@class="old-price"]//text()').extract_first()[:-4].strip())
            #i['proizvodit'] = response.xpath(
            #    "//div[@class='new-info']/p[@class='new-manifacture']/text()").extract()
           #i['category'] = response.xpath("//div[@class='bx-breadcrumb']/*/a[@title]/span/text()").extract()
            #for x in range(15,len(size_dx),-1):
            #    i['size'+str(x)] = ''
            #for g, c in enumerate(size_dx):
            #    i['size'+str(g)] = c

            #except:
            #    pass
            #try:

            #except:
            #    pass
            #
            ##i['tablesize'] = response.xpath("//table[@class='sizetable']").extract()
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
# response.xpath("//span[contains(@style,'background-color')]").extract_first().split('"')[1].split('#')[1]
#  z=' '.join(a.split()) убрать все \n \t  из a

# запускать из домашней папки test командой  scrapy runspider jeans2.py -o bnb55.csv -t csv --nolog
# --nolog это не выводить сообщения
# jeans2.py это имя этого файла
# bnb55.csv это имя файла, куда будет записываться скрап (импорт), можно задать любое имя

#scrapy shell 'https://www.kupi-jeans.ru/zhenskaya_odezhda/dzhinsy/uteplennye_bryuki_dzhinsovye/dzhinsy_zhenskie_uteplennye_miss_bon_mb_702/' --nolog
# запускать оболочку scrapy  для какой-то страницы. тут можно запускать всякие запросы и смотреть что приходит в ответ с этой страницы

#Брюки джинсовые
#Комбинезоны и сарафаны
#Куртки, пиджаки и жилетки
#Распродажа
#Утепленные брюки джинсовые
#Шорты, бриджи, капри
