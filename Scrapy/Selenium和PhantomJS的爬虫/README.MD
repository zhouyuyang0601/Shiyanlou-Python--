#实战目的

学习Selenium和PhantomJS来模拟爬虫之前无法爬取的JavaScript加载的数据

Selenium 是一个 Web 自动化测试工具，最初是为网站自动化测试而开发的。Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的页面，甚至页面截屏，或者判断网站上某些动作是否发生。它支持主流的浏览器，包括 PhantomJS 这个无界面的浏览器。
将 Selenium + PhantomJS 联合使用相当于在代码里面模拟了浏览器

我们可以使用这个组合去抓取一些 JavaScript 渲染的页面，也可以用代码模拟人的一些操作，比如点击按钮，拖动，填写表单等等。

#挑战内容

使用Selenium+PhantomJS模拟实验楼下“用Python抓去2048游戏下所有评论”

目标网页：
https://www.shiyanlou.com/courses/427

#执行过程
python3 spider.py

保存到comments.json中

#实验要求
不能直接爬取AJAX的API接口
不能直接使用Scrapy框架，可以基于Scrapy的HtmlResponse做数据提取
用模拟浏览器的下一页解析下一页数据

#