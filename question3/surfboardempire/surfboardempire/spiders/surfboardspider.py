import scrapy
from surfboardempire.items import SurfboardempireItem  

class SurfboardspiderSpider(scrapy.Spider):
    name = "surfboardspider"
    allowed_domains = ["surfboardempire.com.au"]
    start_urls = ['https://www.surfboardempire.com.au/products.json?page=1']
    page = 1

    def parse(self, response):
        products = response.json().get("products")
        for product in products:
            # print(product)
            product_item = SurfboardempireItem()
            product_item['sku_name'] = product['title']
            product_item['product_id'] = product['id']
            product_item['brand'] = product['vendor']
            product_item['product_url'] = 'https://www.surfboardempire.com.au/products/' + product['handle']
            yield product_item
        if len(product) != 0:
            self.page +=1
            next_page_url = 'https://www.surfboardempire.com.au/products.json?page=' + str(self.page)
            yield response.follow(next_page_url, callback=self.parse)
