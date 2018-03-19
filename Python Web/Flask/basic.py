#coding=utf-8
"""
Flask: Python社区中颇为流行的微框架。具有简单上手，维护简单的特性
"""

#1 调用Flask
#run.py

from flask import flask
app =Flask(__name__)
@app.route('/')
def index():
    return 'hello shiyanlou'
if __name__=='main'
    app.run()

#在调用前需要先设置环境变量
"""
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
环境变量 FLASK_APP 是用来指向 flask run 执行的 Flask 应用代码的路径，这里是 app.py 的路径。
FLASK_DEBUG=1 表示打开 DEBUG 信息，可以输出访问和出错信息，帮助我们解决代码中出现的问题，建议后续只要执行 flask run 都要打开 FLASK_DEBUG
"""
