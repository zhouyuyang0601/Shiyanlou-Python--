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