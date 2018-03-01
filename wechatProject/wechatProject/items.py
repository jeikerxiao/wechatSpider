# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WechatprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    digest = scrapy.Field()
    content_url = scrapy.Field()
    image_url = scrapy.Field()
    author = scrapy.Field()
    pass
