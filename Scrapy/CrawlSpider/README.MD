#CrawlSpider 是比较常用的一种。
相较于 Spider，CrawlSpider 最大的不同是多了一个 rules 属性。
rules 是一个包含 Rule 对象的列表，每个 Rule 对象定义了如何从返回的页面解析接下来要爬取的页面链接的规则。
Rule 对象的默认参数如下：
“
scrapy.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None)
”
#对于该类中的参数，具体含义如下：

-link_extractor 是一个 Link Extractor 对象。 其定义了如何从爬取到的页面提取链接。

-callback 是一个 callable 或 string。从 link_extractor 中每获取到链接时将会调用该函数，该回调函数接受一个 response作为其第一个参数， 并返回一个包含Item 或者是 Request 对象。
-cb_kwargs 包含传递给回调函数的的字典。
-follow 是一个布尔值，指定了根据该规则从 response 提取的链接是否需要跟进。 如果 callback 为 None， follow 默认设置为   True ，否则默认为 False 。
-process_links 是一个 callable 或 string。 从 link_extractor 中获取到链接列表时将会调用该函数。该方法主要用来过滤。
-process_request 是一个 callable 或 string, 用来过滤 request。 该规则提取到每个 request 时都会调用该函数。该函数必须返回一个 request 或者 None。

#爬取的页面URL 
http://flask.pocoo.org/docs/0.12/

item:
    -url
    -text
url为当前页面的链接
text为当前页面的文本

并将这些保存下来的item存储到redis数据库的list结构中，每一个list节点都是一个item
list在redis的key为flask_doc::items

#安装Redis
    # 安装 Redis
    $ sudo apt-get update
    $ sudo apt-get install redis-server

    # 安装 redis-py 模块
    $ sudo pip3 install redis

    # 启动 Redis 服务，写入数据时请不要关闭 Redis 服务!!!
    $ redis-server

#提示
使用 redis-py 库连接 Redis 数据库，具体参考该模块官方文档给出的 示例。
将 item 序列化为 JSON 数据在存入 Redis ，你可能会使用到 Redis 的 redis.lpush() 操作。
使用 re.sub 处理文本替换，re.sub(pattern, repl, string) 提供的参数有:
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。