# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ApprovalRatingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ApprovalItems(scrapy.Item):
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    approving = scrapy.Field()
    disapproving = scrapy.Field()
    unsure = scrapy.Field()