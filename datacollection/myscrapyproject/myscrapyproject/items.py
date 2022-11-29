# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class MyscrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = scrapy.Field()
    hospital = scrapy.Field()
    date= scrapy.Field()
    review = scrapy.Field()
    rating = scrapy.Field()
    start_url = scrapy.Field()
