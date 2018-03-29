#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from pymongo import MongoClient
from datatime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,abort,render_template

app = Flask(__name__)
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='mysql://root@localhost/user'
))
#使用自定义的数据库名称
db=SQLAlchemy(app)
#Mongo数据库
mongo=MongoClient('127.0.0.1',27017).user


class File(db.Model):
    __tablename__='files'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.string(80),unique=True)
    created_time=db.Column(db.DateTime)
    category_id=db.Column(db.Integer,db.ForeignKey('categories,id'))
    category = db.relationship('Category',uselist=False)
    #uselist使得sql返回的东西只是对象而不是列表
    content=db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title=title
        self.created_time=created_time
        self.category=category
        self.content=content

    def add_tag(self,tag_name):
        file_item = mongo.files.find_one({'file_id':self.id})
        #在files表中索取所有的文件
        #findOne()返回的是一个对象
        if file_item:
        #选择所有的文件
            tags=file_item['tags']
            #选择tags列
            if tag_name not in tags:
            #判断tag_name是否在tags列中
                tags.append(tag_name)
                #如果不是，则插入tag
            mongo.files.update_one({'file_id':self.id},{'$set': {'tags': tags}})
            #更新一次
        else:
        #如果不是满足条件的ID
        #那么tags就插入进去
            tags = [tag_name]
            mongo.files.insert_one({'file_id': self.id, 'tags': tags})
        return tags
        
    def remove_tag(self,tag_name):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            try:
                tags.remove(tag_name)
                new_tags = tags
            except ValueError:
                return tags
            mongo.files.update_one({'file_id': self.id}, {'$set' : {'tags': new_tags}})
            return new_tags
        return []
    
    @property
    def tags(self):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            print(file_item)
            return file_item['tags']
        else:
            return []
        pass

class Category(db.Model):
    __tablename__='categories'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    files=db.realtionship('File')

    def __init__(self,name):
        self.name = name

def insert_datas():
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

@app.route('/')
def index():
    return render_template('index.html',files=File.query_all())

@app.route('/files/<int:file_id>')
#<xxx> 表示file_id解析成一个变量
def file(file_id):
    file_item=File.query.get_or_404(file_id)
    #如果没有获取到file_id文件，就抛出404
    return render_template('file.html',file_item=file_item)
  
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),503
  

if __name__ == '__main__':
    #判断是否启动多次插入数据
    db.create_all()
    #因为第一个插入的是Java，所以通过If not查看是否多次插入
    if not Category.query.filter_by(name='Java').first():
            insert_datas()
    app.run()