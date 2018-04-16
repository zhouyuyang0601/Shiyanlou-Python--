#页面跟随
主要学习scrapy.fellow用法
-问题：在页面中爬取相关页面实现链式爬取
-一般思路：for 循环之后接着(urls=url,callback=parse)
-封装：scrapy.fellow(url,callback)

#下载图片
-依赖：安装Image
-设置：使用ImagePiple，在Setting.py中改
-使用：在items中定义images_urls,images这两项
       爬虫中Import自定义的item,并且设置urls为恰当页面元素。

？执行之后没有抓取下来
#多级抓取

#模拟登陆