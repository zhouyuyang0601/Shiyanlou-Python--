#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask，request,render_template

app = Flask(__name__)
#第一个路由器
@app.route('/')
def index():
    #读取并显示Files文件夹中所有json文件的tiles属性

@app.route('/files/<filename>')
def file(filename):
    #类似一个函数？
    """
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面 --自定义
    """
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404