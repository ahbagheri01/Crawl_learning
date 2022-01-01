import json
import os
f = open("poets.json")
poets = json.load(f)
f.close()
i = 0
for p in poets:
    f = open("./lr/spiders/urladdress.txt","w")
    f.write(p["link"])
    f.close()
    #print(p["link"])
    order = "scrapy crawl poet_spider -O ./poems/"+str(p["id"])+".json"
    os.system(order)
    order = "scrapy crawl poet_spider -O ./poems/"+str(p["id"])+".csv"
    os.system(order)