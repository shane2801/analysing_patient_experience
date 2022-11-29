# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
# from itemloaders.processors import TakeFirst, MapCompose, Join
# from w3lib.html import remove_tags

# def cleanup_url(value):
#     return value.split("/")[5]

# def cleanup_date(value):
#     return value.replace("Posted on ", "")

# def cleanup_rating(value):
#     return value.split()[1]

# def cleanup_review(value):
#     return value.replace("\n", ". ")


class ReviewscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # hospital = scrapy.Field(input_processor = MapCompose(remove_tags, cleanup_url), output_processor = TakeFirst())
    # date = scrapy.Field(input_processor = MapCompose(remove_tags, cleanup_date), output_processor = TakeFirst())
    # review = scrapy.Field(input_processor = MapCompose(remove_tags, cleanup_review), output_processor = TakeFirst())
    # rating = scrapy.Field(input_processor = MapCompose(remove_tags, cleanup_rating), output_processor = TakeFirst())

    name = scrapy.Field()
    hospital = scrapy.Field()
    date= scrapy.Field()
    review = scrapy.Field()
    rating = scrapy.Field()
    start_url = scrapy.Field()