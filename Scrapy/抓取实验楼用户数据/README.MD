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