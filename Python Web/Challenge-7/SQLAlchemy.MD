#文档

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#导入模块

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#选择引用的数据库
#在SQL中创建

db = SQLAlchemy(app)
#db变量为SQLAlchemy的函数

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
#primary_key标识是否为主键
#unique是否为独一无二
#string字符类变量
#Integer整数型变量
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

