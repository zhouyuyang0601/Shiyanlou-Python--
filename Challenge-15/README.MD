#文档
https://github.com/shiyanlou?tab=repositories

从页面中爬取下来，#仓库名称 #更新时间 存入json文件

https://github.com/shiyanlou?page={}&tab=repositories

#run

scrapy runspider scrapy.py -o data.json

//*[@id="user-repositories-list"]
#user-repositories-list > ul > li:nth-child(2) > div.d-inline-block.mb-1 > h3 > a
30

#body
//*[@id="user-repositories-list"]


#title
xpath
louplus_python
//*[@id="user-repositories-list"]/ul/li[1]/div[1]/h3/a

//*[@id="user-repositories-list"]/ul/li[1]/div[1]/h3/a

li标签会递增 最多到30

#time
//*[@id="user-repositories-list"]/ul/li[2]/div[3]/relative-time

In [19]: response.xpath('//*[@id="user-repositories-list"]/ul/li[2]/div[3]/relative-time').extract()
Out[19]: ['<relative-time datetime="2018-03-08T09:22:34Z">Mar 8, 2018</relative-time>']

Mar 8, 2018 是text
response.xpath('//*[@id="user-repositories-list"]/ul/li[2]/div[3]/relative-time/@datetime').extract()

