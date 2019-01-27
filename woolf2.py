# -*- coding: utf-8 -*-
import scrapy
from operator import methodcaller
#import time
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


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

    
    name = 'wool'
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
        # print(response)
        # print(str(response)[5:])
        # print(response.xpath('//div[@id="yarnDescription"]/div[@class="d2"]/text()').extract()[0])

        # print(str(response)[5:-2])
        #name_dx = response.xpath('//div[@id="yarnDescription"]/div[@class="d2"]/text()').extract()[0]
        ##name_dx = name_dx.lstrip().rstrip()
        #price_dx = int(response.xpath('//div[@id="yarnDescription"]/p/text()').extract()[4].strip()[:-7])

        #i['name'] = str(response.xpath('//div[@id="yarnDescription"]/div[@class="d2"]/text()').extract()[0])
        # ищет на странице фразу "карта цветов", чтобы понять, что находимся на странице товара
        if len(
                response.xpath(
                    '//div[@id="center"]//h5[contains(text(),"Карта цветов")]'
                ).extract()) >= 1:
            # if (name_dx == 'None') or (len(response.xpath('//div[@id="center"]//h5[contains(text(),"Карта цветов")]').extract()) < 1):  # ищет на странице фразу "карта цветов", чтобы понять, что находимся на странице товара
            #    pass
            # else:
            ur = response.url
            dom = response.meta.get('download_slot')
            i['sku'] = ur[ur.find(dom) + len(dom) + 1:ur.find(dom) + len(dom) +
                          10:].replace('_', '-')
            i['Link'] = str(response)[5:-1]
            #    print(str(response)[5:-2])
            #
            #    i = {}
            #    # response.xpath('//div[@class="descr title-descr"]/h1/text()').extract_first()
            try:
                i['name_v'] = str(
                    response.xpath(
                        '//div[@id="yarnDescription"]/div[@class="d2"]/text()'
                    ).extract()[0])
            except:
                i['name_v'] = 'none'

            try:
                price = int(
                    response.xpath('//div[@id="yarnDescription"]/p/text()').
                    extract()[4].strip()[:-7])
                i['price'] = str(round(price * 1.6, -1))
                i['price_z'] = str(price)
            except:
                i['price'] = 'none'
                i['price_z'] = 'none'

            #  категории
            categ_dx = response.xpath(
                '//div[@id="container"]//div[@id="center"]/p/a/text()'
            ).extract()
            categ_dx = categ_dx[:len(categ_dx)]
            categ_dx = categ_dx[::-1]
            for x in range(0, 6):
                try:
                    i['categor_list' + str(x)] = categ_dx[x]
                except:
                    i['categor_list' + str(x)] = ''
            #for g, c in enumerate(categ_dx):
            #   i['categor_list' + str(g)] = c
            # опции и их значения
            list_options = response.xpath(
                '//div[@id="yarnDescription"]/p/span/text()').extract()
            # ' '.join(response.xpath('//div[@id="yarnDescription"]/p/text()').extract()).split()
            list_options_value = response.xpath(
                '//div[@id="yarnDescription"]/p/text()'.strip()).extract()
            list_options_value2 = map(lambda x: x.strip(), list_options_value)
            #print(type(list_options_value2))
            #list_options_value = map(lambda x: x.remove(None), list_options_value)
            # for x in list_options_value:
            #    x=x.strip()
            # list_options_value.remove('')
            # print('--------')
            list_options_value = []
            #for x,f in enumerate(list_options_value2):
            #if x == "":
            #print('NONE')
            #else:
            #   print(x,' ---*******')
            for code in list_options_value2:
                list_options_value.append(code)
            #print(type(list_options_value))
            #for x,f in enumerate(list_options):
            #    print('---*******')
            #    print(list_options[x])
            #    print(round(int(list_options[x].replace(' руб','')) * 1.6, -1))
            #    print(f)
            #    print('++++*******')
            # print('NONE')
            #else:
            #   print(x,' ---*******')
            #print([x for x in list_options_value if x != ''])
            #mode = [x for x in list_options_value if x != '']
            # mode = [map(methodcaller('strip'), list_options_value)]          74% альпака 18% полиамид 8% шерсть
            try:
                if bf=='wow':
                    pass
            except:
                for x in range(0, 6):
                    i['list_options' + str(x)] = ''
                    i['list_options_value' + str(x)] = ''
                bf='wow'
            #try:
            #    if bfo=='wow':
            #        pass
            #except:
            #    for x in range(0, 90):
            #        i['img_color' + str(x)] = ''
            #        
            #    bfo='wow'
            #try:
            #    if bfp=='wow':
            #        pass
            #except:
            #    for x in range(0, 6):
            #        i['list_img' + str(x)] = ''
            #    bfp='wow'
            # print(mode)
            for t, j in enumerate(list_options_value):
                #    i['list_options' + str(t)] = list_options[t]
                #    i['list_options_value' + str(t)] = j

                # if str(j) != '':
                i['list_options' + str(t)] = list_options[t]
                if (str(j) == '') and (t == 4):
                    i['list_options_value' + str(t)] = round(
                        int(list_options[t + 1].replace(' руб', '')[:-3])
                        * 1.6, -1)
                    i['price_skidka'] = round(
                        int(list_options_value[t + 1].replace(' руб', '')[:-3]) *
                        1.6, -1)
                    break
                else:
                    #print(j.replace(' руб',''))
                    #print('!!!!!!*******')
                    if isInt(j.replace('.00 руб', '')):
                        i['list_options_value' + str(t)] = round(
                            int(j.replace(' руб', '')[:-3]) * 1.6, -1)
                    else:
                        i['list_options_value' + str(t)] = j
#            for x in range(9, len(list_options_value), -1):
                i['list_options' + str(x)] = ''
                i['list_options_value' + str(x)] = ''
            # except:
            #    i['list_options' ] = 'none'
            #    i['list_options_value' ] = 'none'

        # номера цветов  картинки   list(map(lambda x: response.url[:23]+x, sd))
            sd = response.xpath('//div[@id="center"]/table[@class="main"]//tr/td[@class="items_div"]/img[re:match(@src,"jpg")]/@src').extract()  # список картинок
            i['img_color'] = ' ; '.join(list(map(lambda x: response.url[:23]+x, sd)))
            i['name_color'] = ' ; '.join(response.xpath('//div[@id="center"]/table[@class="main"]//tr/td[@class="items_div"]//p[@class="text2"]/text()').extract())
            #  описание
            i['description'] = re.sub( r'[\x00-\x1f\x7f-\x9f-\xa0-]', '', ''.join( response.xpath('//div[@id="uhod"]/text()').extract()). strip()) +   re.sub( r'[\r\n\x00-\x1f\x7f-\x9f-\xa0-]', "", ';'.join( response.xpath('//div[@id="uhod"]//span/text()'). extract()))

            # список картинок
            ad = response.xpath('//div[@id="yarnDescription"]//a[contains(@href,".jpg")]/@href').extract(), response.xpath( '//div[@id="yarnDescription"]//a[contains(@href,".jpg")]/img/@src').extract()
            af =  list(list(map(lambda x: response.url[:23]+''.join(x), ad)))  #''.join(list(map(lambda x: response.url[:23]+''.join(x), ad)))
            i['list_img1'] = af[0]
            i['list_img2'] = af[1]
            #i['list_img'] = ' ; '.join(list(map(lambda x: response.url[:23]+x, af)))
            #  ['sku'] = #'ARK-' + str(response.xpath("//div[@class='new-info']/p[@class='new-article']/text()").extract()).strip('[]').split(':')[1].strip()[:-1]

            i['quantity'] = 20
            i['delivery'] = 2

            #i['Link'] = str(response)[5:-2]
            #
            #i['size'] = response.xpath("//ul[@class='parameters clearfix']/*/a[not(re:match(@class,'[with]'))]/text()").extract()
            # try:
            #
            # ['country_proizvodit'] = response.xpath('//div[@id="center"]//p[@class="status"]/a/text()').extract()[-1]
            ##
            # i['photo'] = 'https://www.kupi-jeans.ru' + response.xpath('//div[@class="image"]/a/@href').extract_first()add_photo_dx = response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
            # for y in range(1, 10):
            # if len(add_photo_dx) > 0:
            # break
            # else:
            # time.sleep(2)
            # add_photo_dx = response.xpath(
            # "//div[@class='catalog_object_thumbs']/*/img/@src"
            # ).extract()
            # break
            ##add_photo_dx = add_photo_dx[:len(add_photo_dx)]
            # for x in range(12, len(add_photo_dx), -1):
            ##    i['add_photo_dx' + str(x)] = ''
            # for t, j in enumerate(add_photo_dx):
            # i['add_photo_dx' + str(t)] = 'https://www.kupi-jeans.ru' + j  #add_photo_dx #'https://www.kupi-jeans.ru'+response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
            # add_photo_dx[t] = 'https://www.kupi-jeans.ru'+ add_photo_dx[t]
            # i['add_photo'+str(t)] = 'https://www.kupi-jeans.ru'+j #add_photo_dx #'https://www.kupi-jeans.ru'+response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
            #

            i['quantity opc'] = '10;10;10;10;10;10;10;10;10;10;10;10;10;10;10;10;10;1010;10;10;10;10;1010;10;10;10;10;10;10;10;10;10'

            # int(response.xpath('//span[@class="old-price"]//text()').extract_first()[:-4].strip())
            # i['proizvodit'] = response.xpath(
            #    "//div[@class='new-info']/p[@class='new-manifacture']/text()").extract()
            #i['category'] = response.xpath("//div[@class='bx-breadcrumb']/*/a[@title]/span/text()").extract()
            # for x in range(15,len(size_dx),-1):
            #    i['size'+str(x)] = ''
            # for g, c in enumerate(size_dx):
            #    i['size'+str(g)] = c

            # except:
            #    pass
            # try:

            # except:
            #    pass
            #
            ##i['tablesize'] = response.xpath("//table[@class='sizetable']").extract()
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
