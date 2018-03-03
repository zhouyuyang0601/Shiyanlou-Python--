#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
from flask import Flask,abort,render_template

app = Flask(__name__)
"""
app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。 
    让flask.helpers.get_root_path函数通过传入这个名字确定程序的根目录，以便获得静态文件和模板文件的目录。 
所以一般是在#根目录#下面允许程序
"""
class read_file(obejct):
    #返回根目录下的files文件夹目录
    #因为我们已知Json文件会被存储在files中
    #所以在类变量中声明directory
    directory = os.path.join(os.path.abspath(os.path.dirname(__name__)),'..','files')

    """
    os.path.join
    join(a, *p)
    将目录名和文件的基名拼接成一个完整的路径
    
    os.path.abspath
    返回一个目录的绝对路径
    Return an absolute path.

    os.path.dirname
    返回一个目录的目录名
    Returns the directory component of a pathname
    """
    def __init__(self):
        self._files=self._read_all_files()
    
    def _read_all_files(self):
        result={}
        for filename in os.listdir(self.directory):
            """
            os.listdir()
            方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
            """
            file_path =  os.path.join(self.direcotry,filename)
            with open(file_path) as f:
                result[filename[:-5]]=json.load(f)
                #'.json 一共5个字符
                #去掉最后的5个字符就留下前面的部分
        return result
    """
    result一整个是一个字典格式变量，通过如下格式来读取数据

    result:
    -helloshiyanlou：        -helloworld：
     {-title                  {-title
      -created_time            -created_time
      -content}                -content}
    其中的helloshiyanlou, helloworld各自又是一个由字典组成的文件
    title,created_time,content各自都是字典，包含键与值
    """

    def get_title_list(self):
        return [item['title'] for item in self._files.valus()]
    
    def get_by_filename
        return self._files.get(filename)

files=read_file()

#根目录
@app.route('/')
def index():
    return render_template('index.html',title_list=files.get_title_list())
"""
定义title_list变量
在index.html中 由 {% for title in title_list %}来操作
Jinja2需要{%end for%}来完成所有变量
"""

@app.route('/files/<filename>')
def file(filename):
    file_item=files.get_by_filename(filename)
    if not file_item
        abort(404)
    return render_template('file.html',file_item=file_item)
    """
    1.os.path查看目录
        通过read_file()类实现了
    2.是：序列化并提取渲染
        在类中，通过json.load()实现
    3.否：返回自定义404页面
        判断file_item文件是否在files文件夹下，若不在，则报404
        若是，则转到file.html
    """
@app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'),404
    """
    输出自定义的404页面
    """

if __name__='__main__':
    app.run()