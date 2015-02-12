# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InboxItem(scrapy.Item):
    # define the fields for your item here like:
    folder = scrapy.Field()
    id = scrapy.Field()
    sender_name = scrapy.Field()
    sender_profile_url = scrapy.Field()
    to_name = scrapy.Field()
    to_profile_url = scrapy.Field()
    subject = scrapy.Field()
    date = scrapy.Field()
    is_replied = scrapy.Field()
    body = scrapy.Field()
    pass
