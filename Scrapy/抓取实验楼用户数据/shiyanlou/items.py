# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class UserItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    job = scrapy.Field()
    school = scrapy.Field()
    level = scrapy.Field()
    join_date = scrapy.Field()
    learn_courses_num = scrapy.Field()

