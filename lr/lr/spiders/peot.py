import scrapy
from scrapy import item
from ..items import LrItem
class Ganjoor_spider(scrapy.Spider):
    name = 'poet_spider'
    base = "https://ganjoor.net/"
    urls = []
    with open("./lr/spiders/urladdress.txt") as file:
        for line in file:
            urls.append(line.rstrip())
    print(urls)
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        all_div_cols = response.css('#garticle').css("p").css("a")
        for quote in all_div_cols:
            title = quote.xpath("text()").extract_first()
            link= quote.xpath('@href').extract()[0]
            yield {
                "title":title,
                "link":self.base + link
            }
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