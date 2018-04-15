#目标
获得制定用户的Github的所有仓库，并且将数据存储进入数据库中
https://github.com/shiyanlou?tab=repositories

#数据库
利用sqlalchemy创建数据库表repositories，并且连接数据库，包含下列格式：
class Repository(Base)：
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key = Ture)
    name = Column(String(64))
    update_time = Column(DateTime)

#环境依赖
sudo pip install sqlalchemy

#robots.txt
在setting.py下将robostxt_Obey设为False

#知识点

Scrapy 项目框架
分析网页元素字段
SQLAlchemy 定义数据模型
连接数据库
创建 Scrapy 项目
创建爬虫
Item 容器
Item Pipeline
Models 创建表
保存 Item 到数据库