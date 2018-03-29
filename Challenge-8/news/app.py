from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import event
from pymongo import MongoClient
from datetime import datetime
"""
sqlALchemy用于操作MySQL
Pymonog用于操作MongoDb
"""

app=Flask(__name__)

app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'mysql://root@127.0.0.1/news'
})
#定义数据库 db(mySQL) mongo(MongoDB)
db=SQLAlchemy(app)
mongo=MongoClient('127.0.0.1',27017)

class File(db.Model):

    __tablename__= 'files'
    #id作为整数型，作为数据库的主键
    id=db.Column(db.Integer,primary_key=True)
    #Title是作为一个索引，不能重复的
    title=db.Column(db.string(80),unique=True)
    category_id=db.Column(db.Integer,db.ForeignKey('categories.id'))
    category = db.relationship('Category',uselist=False)
    """
    category_id是一个外键，关联到categories的id中
    uselist为False的时候返回是一个对象，在默认情况下是一个列表
    """

    content=db.Column(db.Text)

    created_at=db.Column(db.Datetime,default=datetime.utcnow)
    updated_at=db.Column(db.Datetime,default=datetime.utcnow)
    """
    对象的创建时间和更新时间区别开来
    utc时间能够保证各个时区显示正确（海外用户)
    """

    def add_tag(self,tag):
        mongo.file.update.one({'_id':self.id},{'%addToSet':{'tags':tag}})
        return self._file['tags']

    def remove_tag(self,tag):
        mongo.file.update.one({'_id':self.id},{'%pull':{'tags':tag}})
        return self._file['tags']

    @property 
    def mongo(self):
        return mongo.file.find_one({'_id':self.id})

    @property
    def tags(self):
        return self._file['tags']
"""
File对象插入数据时，自动创建关联的MongoDb对象
"""
@event.listens_for(File,'after_insert')
def auto_crate(mapper,conn,file):
    mongo.file.insert_one({'_id':file.id})
#File移除时，自动删除Mongo对象
@event.listens_for(File, 'after_delete')
def auto_delete_mongodb_file(mapper, conn, file):
    mongo.file.delete_one({'_id': file.id})

"""
开始写Category类
映射到Category表中，与上文相对应
"""

class Category(db.Model):

    __tablename__="Categories"

    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    files=db.relationship("File")

    def __init__(self,name):
        self.name = name

@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())

@app.route('/files/<int:file_id>')
def file(file_id):
    file = File.query.get_or_404(file_id)
    """
    由file.id在File数据库中去获取file
    当没有取得对应的File_id的时候，抛出错误异常
    """
    return render_template('file.html',file=file)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
    """
    在返回render_template可以返回多个结果，在处理时将第二个值（404）作为状态码
    """

def  insert_datas():
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')


if __name__=='__main__':
    
    #启动应用时插入数据
    db.create_all()
    if Category.query.filter_by(name='Java').first():
        insert_datas()
    app.run()

