# -*- coding: utf-8 -*-
import scrapy

from lab4.items import Lab4Item


class CoursesImageSpider(scrapy.Spider):
    name = 'courses_image'
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        item = Lab4Item()
        item['images_urls'] = response.xpath('//div[@class="course-img"]/img/@src').extract()
        yield item
