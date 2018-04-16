# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Lab4Item(scrapy.Item):
    images_urls=scrapy.Field()
    images = scrapy.Field()
