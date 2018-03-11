#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
import json
from datatime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,abort,render_template

app = Flask(__name__)
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='mysql://root@localhost/user'
))
#使用自定义的数据库名称
db=SQLAlchemy(app)

class File(db.Model):
    __tablename__='files'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.string(80),unique=True)
    created_time=db.Column(db.DateTime)
    category_id=db.Column(db.Integer,db.ForeignKey('categories,id'))
    category = db.relationship('Category',uselist=False)
    content=db.Column(db.Text)

    def __init__(self,title,created_time,category,contet):
        self.title=title
        self.created_time=created_time
        self.category=category
        self.content=content

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

@app.route('/')
def index():
    return render_template('index.html',title_list=files.get_title_list())

@app.route('/files/<filename>')
def file(filename):
    file_item=files.get_by_filename(filename)
    if not file_item:
        abort(404)
    return render_template('file.html',file_item=file_item)
  
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
  

if __name__ == '__main__':
    app.run()