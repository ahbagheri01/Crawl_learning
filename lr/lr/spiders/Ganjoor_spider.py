import scrapy

class Ganjoor_spider(scrapy.Spider):
    name = 'Ganjoor_spider'
    start_urls = ["https://quotes.toscrape.com/"]


   # def parse(self, response, **kwargs):
     #   return super().parse(response, **kwargs)

    def parse(self, response,** kwargs):
        title = response.css('title::text').extract()
        yield {
            'title':title
        }
    

