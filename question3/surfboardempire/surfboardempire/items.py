# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SurfboardempireItem(scrapy.Item):
     sku_name = scrapy.Field()
     product_id = scrapy.Field()
     brand = scrapy.Field()
     product_url = scrapy.Field()
