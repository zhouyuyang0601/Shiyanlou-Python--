#知识点
创建数据库
创建scrapy项目
创建爬虫
item容器
itme pipeline
Models创建表
保存item到数据库
item过滤

#目的
scrapy返回的dict文件是无序的，通过使用item将结构化数据保存下来转存到数据库中

#创建数据库
 -将MySQL编码格式改成utf-8
 ""
 sudo vim /etc/mysql/my.cnf
 [client]
default-character-set = utf8

[mysqld]
character-set-server = utf8

[mysql]
default-character-set = utf8

-启动Mysql
sudo service mysql start

-进入mysql
mysql -uroot

-创建数据库
mysql > create database shiyanlou;

#创建项目
scrapy startproject shiyanlou

-项目结构
shiyanlou/
    scrapy.cfg            # 部署配置文件
    shiyanlou/            # 项目名称
        __init__.py
        items.py          # 项目 items 定义在这里
        pipelines.py      # 项目 pipelines 定义在这里
        settings.py       # 项目配置文件
        spiders/          # 所有爬虫写在这个目录下面
            __init__.py

#创建爬虫
使用genspider快速初始化模板
scrapy genspider <name> <domain>

#创建item
使用scrapy.Field()定义一个变量是item变量
在items.py中写入所有需要定义的格式

定义之后在spiders文件夹下的爬虫中
    1.from <projectname>.items import <itemname>
    2.同时在Parse中，把爬虫获取的结果封装成courseitem格式

spider相當於是制作物品的生产线，Item相当于包装盒

#创建Pipeline模版
Pipeline 对 Item 进行这几项处理：

-验证爬取到的数据 (检查 item 是否有特定的 field)
-检查数据是否重复
-存储到数据库
##process_item
处理完成之后返回一个item 对象
##open_spider
##close_spider
两个Hook函数

#models.py
用sqlalchemy的语法定义course表的数据库结构

