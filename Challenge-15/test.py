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
				'name':repositories.xpath('//*[@id="user-repositories-list"]/ul/li[2]/div[1]/h3/a/text()').extract_first().strip(),
				'update_time':repositories.xpath('//*[@id="user-repositories-list"]/ul/li[2]/div[3]/relative-time/@datetime').extract()
			}	
