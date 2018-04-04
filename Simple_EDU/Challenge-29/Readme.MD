#start from Simple-EDU lab 1
    增加一个新的Blueprint 支持用户个人页面

#下载完整的代码
下载代码文件并解压
$ wget http://labfile.oss.aliyuncs.com/courses/923/week7/code/lab1.zip

#测试数据
$ sudo service mysql start
$ mysql -uroot
> create database simpledu;
$ export FLASK_APP=manage.py
$ export FLASK_DEBUG=1
$ flask shell
##增加了User数据库
>>> from simpledu.models import db, User, Course
>>> db.create_all()
>>> user = User(username='admin')
>>> course1 = Course(name='python course', author=user)
>>> course2 = Course(name='flask course', author=user)
>>> db.session.add(user)
>>> db.session.add(course1)
>>> db.session.add(course2)
>>> db.session.commit()

#服务启动命令
flask run

#实验要求
增加新的路由支持这个页面 localhost:5000/user/<username> 中显示用户 id，username 和这个用户发布的课程名称列表。

#目标
    -增加新的 user 蓝图
    -蓝图中的路由可以支持用户主页的显示
    -提交结果的时候请保证 Flask 处于运行状态，既 http://localhost:5000 可以连接
    -后台会对 localhost:5000/user/admin 页面进行测试，查看是否包含 admin 用户的用户名，id 和课程名称列表（python -course 和 flask course字符串），请确保页面中有这些内容

