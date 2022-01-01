import scrapy
from scrapy import item
from ..items import LrItem
class Ganjoor_spider(scrapy.Spider):
    name = 'Ganjoor_spider'
    start_urls = ["https://ganjoor.net/"]
    id = 1
    authors = {}
    def parse(self, response):
        items = LrItem()
        all_div_cols = response.css('div.poet').css("a")
        for quote in all_div_cols:
            title = quote.xpath('@title').extract()
            if (len(title)) <= 0:
                continue
            title = title[0]
            author= quote.xpath('@href').extract()[0]
            items["title"] = title
            items["author"] = author
            items["link"] = self.start_urls[0] + author
            items["id"] = self.id
            yield items
            self.id +=1
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