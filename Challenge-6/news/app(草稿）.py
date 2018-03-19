#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
from flask import Flask,abort,render_template

app = Flask(__name__)
#第一个路由器
@app.route('/')
def index():
    #读取并显示Files文件夹中所有json文件的tiles属性
    """
    1.os模块读取json文件列表
    2.json序列化转为字典
    3.render_templates生成页面
    """
    filelist=os.listdir('/home/shiyanlou/files/')
    for files in filelist:
        i=0
        with open(file) as f:
            'file_'st+=json.loads(file)
        

@app.route('/files/<filename>')
def file(filename):
    #类似一个函数？
    """
    1.os.path查看目录
    2.是：序列化并提取渲染
    3.否：返回自定义404页面
    """
@app.errorhandler(404)
    """
    输出自定义的404页面
    """
def not_found(error):
    return render_template('404.html'), 404