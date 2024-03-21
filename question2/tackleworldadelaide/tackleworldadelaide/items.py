# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TackleworldadelaideItem(scrapy.Item):
    sku_name = scrapy.Field()
    image_url = scrapy.Field()
    price_now = scrapy.Field()
    price_was = scrapy.Field()
    product_url = scrapy.Field()
