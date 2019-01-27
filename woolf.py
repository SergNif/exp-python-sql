# -*- coding: utf-8 -*-
import scrapy
from operator import methodcaller
#import time
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WoolSpider(CrawlSpider):
    name = 'wool'
    allowed_domains = ['terrakot-yarn.ru']
    start_urls = ['http://terrakot-yarn.ru']

    rules = (Rule(
        LinkExtractor(
            #allow = 'terrakot-yarn.ru'#r'terrakot-yarn.ru/',#allow=r'zhenskaya_odezhda/dzhinsy/',
            #deny=('pryazha')  #, 'COUNT', 'filter'),
        ),
        callback='parse_item',
        
        follow=True), )
    

    def parse_item(responsef, response):
        #print(response)
        #print(str(response)[5:])
        #print(response.xpath('//div[@id="yarnDescription"]/div[@class="d2"]/text()').extract()[0])
 
        #print(str(response)[5:-2])
        #name_dx = response.xpath('//div[@id="yarnDescription"]/div[@class="d2"]/text()').extract()[0]
        ##name_dx = name_dx.lstrip().rstrip()
        i = {}
        #price_dx = int(response.xpath('//div[@id="yarnDescription"]/p/text()').extract()[4].strip()[:-7])
        #i['name'] = str(response.xpath('//div[@id="yarnDescription"]/div[@class="d2"]/text()').extract()[0])
        if len(response.xpath('//div[@id="center"]//h5[contains(text(),"Карта цветов")]').extract()) >= 1:  # ищет на странице фразу "карта цветов", чтобы понять, что находимся на странице товара
        #if (name_dx == 'None') or (len(response.xpath('//div[@id="center"]//h5[contains(text(),"Карта цветов")]').extract()) < 1):  # ищет на странице фразу "карта цветов", чтобы понять, что находимся на странице товара
        #    pass
        #else:
           
            i['Link'] = str(response)[5:-1]
        #    print(str(response)[5:-2])
#
        #    i = {}
        #    # response.xpath('//div[@class="descr title-descr"]/h1/text()').extract_first()
            try:
                i['name_v'] = str(response.xpath('//div[@id="yarnDescription"]/div[@class="d2"]/text()').extract()[0])
            except:
                i['name_v'] = 'none'

            try:
                price = int(response.xpath('//div[@id="yarnDescription"]/p/text()').extract()[4].strip()[:-7])
                i['price'] = str(price * 1.6)
                i['price_z'] = str(price)
            except:
                i['price'] = 'none'
                i['price_z'] = 'none'

            #try:
            # опции и их значения
            list_options = response.xpath('//div[@id="yarnDescription"]/p/span/text()').extract()
            list_optoins_value = response.xpath('//div[@id="yarnDescription"]/p/text()'.strip()).extract()#' '.join(response.xpath('//div[@id="yarnDescription"]/p/text()').extract()).split()
            list_optoins_value2 = map(lambda x: x.strip(), list_optoins_value)
            #list_optoins_value = map(lambda x: x.remove(None), list_optoins_value)
            #for x in list_optoins_value:
            #    x=x.strip()
            #list_optoins_value.remove('')
            #print('--------')
            #for x,f in enumerate(list_optoins_value2):
            ##    if x == "":
            ##        print('NONE')
            ##    else:
            #    print(x,' ---*******')
            ##        for code in map(ord, x):
            #    print(f)
            #    print(list_options[x])
            #    print('*******')
            #print('--------')
            #print([x for x in list_optoins_value if x != ''])
            #mode = [x for x in list_optoins_value if x != '']
            #mode = [map(methodcaller('strip'), list_optoins_value)]          74% альпака 18% полиамид 8% шерсть
            #print(mode)
            for t, j in enumerate(list_optoins_value2):  #for m in resp_foto:
                #if str(j) != '':
                i['list_optoins' + str(t)] = list_optoins[t]
                i['list_optoins_value' + str(t)] = j
            for x in range(9, len(list_optoins_value2), -1):
                i['list_options' + str(x)] = '' 
                i['list_optoins_value' + str(x)] = ''
            #except:
            #    i['list_options' ] = 'none'
            #    i['list_optoins_value' ] = 'none'
            
            
            

          

          # номера цветов  картинки
            i['list_img']=response.xpath('//div[@id="center"]/table[@class="main"]//tr/td[@class="items_div"]/img[re:match(@src,"jpg")]/@src').extract() #список картинок


         #  описание
            i['description'] = re.sub(r'[\x00-\x1f\x7f-\x9f-\xa0-]', '', ''.join(response.xpath('//div[@id="uhod"]/text()').extract()).strip()) + re.sub(r'[\r\n]',"",';'.join(response.xpath('//div[@id="uhod"]//span/text()').extract()))


         #  категории
            #categ_dx = response.xpath('//div[@id="container"]//div[@id="center"]/p/a/text()').extract()
            #categ_dx = categ_dx[:len(categ_dx)]
            #for x in range(10, len(categ_dx), -1):
            #    i['categor_list' + str(x)] = ''
            #for g, c in enumerate(categ_dx):
            #    i['categor_list' + str(g)] = c
#
            #список картинок
            i['img_color'] = [response.xpath('//div[@id="yarnDescription"]//a[contains(@href,".jpg")]/@href').extract(),response.xpath('//div[@id="yarnDescription"]//a[contains(@href,".jpg")]/img/@src').extract()]
            i['name_color'] = response.xpath('//div[@id="center"]/table[@class="main"]//tr/td[@class="items_div"]//p[@class="text2"]/text()').extract()


         #  ['sku'] = #'ARK-' + str(response.xpath("//div[@class='new-info']/p[@class='new-article']/text()").extract()).strip('[]').split(':')[1].strip()[:-1]        
            
            i['quantity'] = 10
            
            #i['Link'] = str(response)[5:-2]
#
            #i['size'] = response.xpath("//ul[@class='parameters clearfix']/*/a[not(re:match(@class,'[with]'))]/text()").extract()
            ##try:
#
            #['country_proizvodit'] = response.xpath('//div[@id="center"]//p[@class="status"]/a/text()').extract()[-1]
##
            #i['photo'] = 'https://www.kupi-jeans.ru' + response.xpath('//div[@class="image"]/a/@href').extract_first()add_photo_dx = response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
            ##for y in range(1, 10):
            ##    if len(add_photo_dx) > 0:
            ##        break
            ##    else:
            ##        time.sleep(2)
            ##        add_photo_dx = response.xpath(
            ##            "//div[@class='catalog_object_thumbs']/*/img/@src"
            ##        ).extract()
            ##        #break
            ##add_photo_dx = add_photo_dx[:len(add_photo_dx)]
            ##for x in range(12, len(add_photo_dx), -1):
            ##    i['add_photo_dx' + str(x)] = ''
            ##for t, j in enumerate(add_photo_dx):
            ##    i['add_photo_dx' + str(t)] = 'https://www.kupi-jeans.ru' + j  #add_photo_dx #'https://www.kupi-jeans.ru'+response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
            ##    #add_photo_dx[t] = 'https://www.kupi-jeans.ru'+ add_photo_dx[t]
            ##    #i['add_photo'+str(t)] = 'https://www.kupi-jeans.ru'+j #add_photo_dx #'https://www.kupi-jeans.ru'+response.xpath("//div[@class='catalog_object_thumbs']/*/img/@src").extract()
#

            i['quantity opc'] = '10;10;10;10;10;10;10;10;10'
            
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

#if __name__ == '__main__':
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
#scrapy runspider wool.py -o wool55.csv -t csv --set CLOSESPIDER_ITEMCOUNT=50 --nolog

#scrapy shell 'https://www.kupi-jeans.ru/zhenskaya_odezhda/dzhinsy/uteplennye_bryuki_dzhinsovye/dzhinsy_zhenskie_uteplennye_miss_bon_mb_702/' --nolog
# запускать оболочку scrapy  для какой-то страницы. тут можно запускать всякие запросы и смотреть что приходит в ответ с этой страницы

#Брюки джинсовые
#Комбинезоны и сарафаны
#Куртки, пиджаки и жилетки
#Распродажа
#Утепленные брюки джинсовые
#Шорты, бриджи, капри
