# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.item


class WhitehousebriefingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class BriefingItem(scrapy.Item):
    url= scrapy.Field()
    title= scrapy.Field()
    briefing_type= scrapy.Field()
    date= scrapy.Field()
    content = scrapy.Field()