import scrapy
from tackleworldadelaide.items import TackleworldadelaideItem  

class TackleworldSpider(scrapy.Spider):
    name = "tackleworld"
    allowed_domains = ["tackleworldadelaide.com.au"]
    start_urls = ["https://tackleworldadelaide.com.au"]

    def parse(self, response):
        categories = response.xpath('//ul[contains(@class, "navPages-list--categories")]/li[@class="navPages-item"]')
        for category in categories:
            subcategories= category.xpath('.//ul[contains(@class, "navPage-subMenu-list")]/li[@class="navPage-subMenu-item"]')
            for subcategory in subcategories:
                subcategory_url = subcategory.xpath('.//a/@href').get()
                yield scrapy.Request(url=subcategory_url, callback=self.parse_category)
    def parse_category(self, response):
        products = response.xpath('//li[contains(@class, "product")]')
        for product in products:
            product_item = TackleworldadelaideItem()
            print(product.xpath('.//span[@class="price price--rrp"]/text()').get())
            product_item['sku_name'] = product.xpath('.//h4/a/text()').get()
            product_item['image_url'] = product.xpath('.//figure[@class="card-figure"]/a/img/@src').get()
            product_item['price_now'] = product.xpath('.//span[@class="price"]/text()').get()
            product_item['price_was'] = product.xpath('.//span[@class="price price--rrp"]/text()').get()
            product_item['product_url'] = product.xpath('.//h4/a/@href').get()
            yield product_item

        # Follow pagination links
        next_page = response.xpath('//li[contains(@class, "pagination__item--next")]/a/@href')
        if next_page:
            yield response.follow(next_page[0], self.parse_category)

