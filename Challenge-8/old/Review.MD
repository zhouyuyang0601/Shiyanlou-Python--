#文档
使用mysqlclient, Flaks_SQLAlchemy

#要求
为挑战六和挑战7的代码添加两个方法和一个属性
    #添加标签
    def add_tag(self,tag_name)
    #移除标签
    def remove_tag(self,tag_name)
    #标签列表
    @property
    def tags(self):
        #读取Mongodb里的东西
#测试
    from app import *
    db.create_all()
    # 增加 MySQL 中的数据
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

    # 增加 MongoDB 中的数据
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')

#修改
修改index以符合页面展示

#提示
MongoDB 内的数据存储格式需要自己定义，需要保证能够通过文章 id 获取得到标签列表
注意考虑如何在 add_tag 的时候避免重复添加相同的标签给同一个文章
当 remove_tag 去掉文章中不存在的标签的时候，不需要报错


=========================================================================
同时使用MongoDB和Mysql
关系数据库和非关系数据库