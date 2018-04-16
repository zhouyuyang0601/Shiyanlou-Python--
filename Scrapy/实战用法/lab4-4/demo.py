# -*- coding: utf-8 -*-
import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'

    start_urls = ['https://www.shiyanlou.com/login']

    def parse(self, response):
        """ 模拟登录的核心就在这里，scrapy 会下载 start_urls 里的
        登录页面，将 response 传到这里，然后调用 FormRequest
        模拟构造一个 POST 登录请求。FormRequest 继承自 Request，
        所以 Request 的参数对它适用。FormRequest 有一类方法 `from_response` 用于快速构建 FormRequest 对象。from_response 方法会从第一步返回的 response 中获取请求的 url，form 表单信息等等，我们只需要指定必要的表单数据和回调函数就可以了。
        """
        return scrapy.FormRequest.from_response(
             # 第一个参数必须传入上一步返回的 response
             response,
             # 以字典结构传入表单数据
             formdata={},
             # 指定回调函数
             callback=self.after_login
        )

    def after_login(self, response):
        """ 登录之后的代码和普通的 scrapy 爬虫一样，构造 Request，指定 callback ...
        """
        pass

    def parse_after_login(self, response):
        pass