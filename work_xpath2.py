import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = ['https://www.kupi-jeans.ru/zhenskaya_odezhda/dzhinsy/bryuki_dzhinsovye/dzhinsy_zhenskie_denim_ht_9015/',]
    allowed_domains = ['kupi-jeans.ru',]


    def parse(self, response):
        for quote in response.xpath('//div[@class="item"]'):
            yield {
                'text': quote.xpath('//div[@class="descr title-descr"]/h1/text()').extract_first(),
                'price': quote.xpath('//span[@class="new-price"]/text()').extract_first(),
                'img': quote.xpath('//div[@class="image"]/a/@href').extract()
            }

        next_page_url = response.xpath('//div[@class="pages"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


        #    //*[@id="main"]
        #    /html/body/div[5]/div[4]/div[4]/div[2]/div/div[2]
        #    descr title-descr
        #    catalog_object_thumbs
        #    item MagicThumb-swap
        