# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TackleworldadelaidePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # Clean up price fields
        if adapter.get("price_now") is not None:
            adapter['price_now'] = self.clean_price(adapter['price_now'])
        if adapter.get("price_was") is not None:
            adapter['price_was'] = self.clean_price(adapter['price_was'])
        return item

    def clean_price(self, price_str):
        cleaned_price = price_str.replace('AUD', '').replace('RRP', '')
        return cleaned_price.strip()

