import scrapy
from scrapy import item
from ..items import LrItem
class Ganjoor_spider(scrapy.Spider):
    name = 'Ganjoor_spider'
    start_urls = ["https://quotes.toscrape.com/"]
   # def parse(self, response, **kwargs):
     #   return super().parse(response, **kwargs)

    def parse(self, response):
        items = LrItem()
        all_div_cols = response.css('div.quote')
        for quote in all_div_cols:
            title = quote.css('span.text::text').extract()
            author= quote.css('.author::text').extract()
            teg = quote.css('.tag::text').extract()
            items["title"] = title
            items["author"] = author
            items["tag"] = teg
            yield items



# scrapy shell 'https://quotes.toscrape.com/'
#response.css("title::text").extract_first()
# https://quotes.toscrape.com/
#response.css("span.text::text")[0].extract()  for class . 
#response.css("span#text::text")[0].extract()  for id #
#  selector gadget chrome
#response.css(".author::text")[0].extract()
# Xpath selectors
#response.xpath("//title/text()").extract()
# response.xpath("//span[@class = 'text']/text()").extract()
#response.xpath("//span[@class = 'text']/text()")[0].extract()
# response.css("li.next a").xpath("@href").extract()
# response.css("a").xpath("@href").extract()