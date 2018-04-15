# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class GithubSpider(scrapy.Spider):
    name = 'github'

    @property 
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self,response):
        for repository in response.css('li.public'):
	        item = ShiyanlougithubItem({
				'name':repositories.css('a[itemprop="name codeRepository"]::text').extract_first().strip(),
				'update_time':repositories.css('relative-time::attr(datetime)').extract_first()
            })
            yield item
        
    def parse(self,response):
		for repositories in response.css('li.public'):
			yield{
				'name':repositories.css('a[itemprop="name codeRepository"]::text').extract_first().strip(),
				'update_time':repositories.css('relative-time::attr(datetime)').extract_first()
			}	
