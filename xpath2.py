import scrapy


class ToScrapeSpiderXPath(scrapy.Spider,resp):
    name = 'toscrape-xpath'
    start_urls = ['https://www.kupi-jeans.ru/zhenskaya_odezhda/dzhinsy/',]
    allowed_domains = ['kupi-jeans.ru',]


    def parse(self, response):
        #for quote in 
        a = resp#response.xpath('//div[@class="item"]')
        yield {
                'text': a.xpath('//div[@class="descr title-descr"]/h1/text()').extract_first(),
                'price': a.xpath('//span[@class="new-price"]/text()').extract_first(),
                'img': a.xpath('//div[@class="image"]/a/@href').extract_first()
            }

        next_page_url = response.xpath('//*[@id="catalog_products"]//div[@class="main-item"]/a/@href').extract_first()
        #next_page_url = response.xpath('//div[@class="pages"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        
if __name__ == '__main__':
    main()

def main():

    for x in xrange(1,int(response.xpath('//div[@class="pages"]/a/@href').extract()[-2].split('=')[-1])+1):
        #else:
            a = response.xpath('//*[@class="pages"]/a/@href').extract_first()
            #url = response.xpath('//*[@class="pages"]/a/@href').extract_first()
            next_page_url = url
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))

        #    //*[@id="main"]
        #//*[@id="catalog_products"]

        #'https://www.kupi-jeans.ru/zhenskaya_odezhda/dzhinsy'+