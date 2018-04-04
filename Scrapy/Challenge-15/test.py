import scrapy

class test(scrapy.Spider):
	
	name='test'

	@property
	def start_urls(self):
		url_temp='https://github.com/shiyanlou?page={}&tab=repositories'
		return (url_temp.format(i) for i in range(1,5))

	def parse(self,response):
		for repositories in response.css('li.public'):
			yield{
				'name':repositories.css('a[itemprop="name codeRepository"]::text').extract_first().strip(),
				'update_time':repositories.css('relative-time::attr(datetime)').extract_first()
			}	
