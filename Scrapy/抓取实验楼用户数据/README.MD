#准备工作
1.修改MySQL配置
sudo vim /etc/mysql/my.cnf
添加以下几个配置：

[client]
default-character-set = utf8

[mysqld]
character-set-server = utf8

[mysql]
default-character-set = utf8

2.进入MySQL修改配置
sudo service mysql start
以 root 身份进入 mysql，实验环境默认是没有密码的：

mysql -uroot
创建 shiyanlou 库给本实验使用：

mysql > create database shiyanlou;

3.按照依赖条件
mysqlclient
sqlalchemy

4.创建项目
scrapy startproject shiyanlou
scrapy genspider users shiyanlou.com

#抓取的数据
要爬取的内容和字段名称定义：

   -用户名（name）
   -类型：普通用户／会员／高级会员（type）
   -加入实验楼的时间（join_date）
   -楼层数（level）
   -状态：在职／学生（status）
   -学校（如果用户是学生）（school）
   -职位（如果用户在职）(job）
   -学习记录（study_record）

#定义数据类型
models.py中course定义user模型

>>
>> User 表用到新类型要引入
from sqlalchemy import Date

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    type = Column(String(64))
    status = Column(String(64), index=True)
    school = Column(String(64))
    job = Column(String(64))
    level = Column(Integer, index=True)
    join_date = Column(Date)
    learn_courses_num = Column(Integer)
>>

#创建item
在items.py中创建UserItem，为每个爬取的字段声明Field
>>
class UserItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    job = scrapy.Field()
    school = scrapy.Field()
    level = scrapy.Field()
    join_date = scrapy.Field()
    learn_courses_num = scrapy.Field()
>>

#Parse文件

1.Name:
response.css('span.username::text')

2.Type:
response.css('a.member-icon img.user-icon:attr(title)').extract_first(default='Normal User')

3.join_date
response.css('span.join-date::text').extract_first()
>>>
def parse(self, response):
        yield UserItem({
            'name': response.css('span.username::text').extract_first(),
            'type': response.css('a.member-icon img.user-icon::attr(title)').extract_first(default='普通用户'),
            'status': response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(),
            'job': response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
            'school': response.xpath('//div[@class="userinfo-banner-status"]/a/text()').extract_first(),
            'join_date': response.css('span.join-date::text').extract_first(),
            'level': response.css('span.user-level::text').extract_first(),
            'learn_courses_num': response.css('span.latest-learn-num::text').extract_first()
        })
>>>

