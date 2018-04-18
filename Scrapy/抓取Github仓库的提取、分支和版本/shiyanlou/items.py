import scrapy


class GithubItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    update_time = scrapy.Field()
    branches = scrapy.Field()
    commits = scrapy.Field()
    releases = scrapy.Field()