#文档
1.安装 mysqlclient FLask_SQLAlchemy
2.手动启动SQL
-sudo service mysql start
my sql -u root
CREATE databases XXX
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/你创建的数据库名称'

3.在FLASK_SQLalchemy中存在两个表
    -文章表                            -类别表
    -Class File(db.Model)              -Class Category(db.Model)
文章都要有，且属于一个类别
M:1

4.文章表：
id (db.Integer)
title (db.String(80))
created_time (db.DateTime)
category_id (db.Integer,db.ForeginKey)
content (db.Text)

5.类比表
id: (db.Integer)
Name (db.String(80))


#Flask_SQLalchemy
http://www.pythondoc.com/flask-sqlalchemy/quickstart.html

#测试
FLASK_Shell中：
db.create_all()
java = Category('Java')
python = Category('Python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()

#主界面
@app.route('/')
def index():
    #显示文章列表
    #显示所有Title,每个标题都使用'<a href=XXX></a>'对应到相应文章页面

@app.route('/files/<file_id>')
def file(file_id)
    #file_id为File文件中的iD
    #需要显示file_id对应的文章内容、创建内容和类别
    #如果不在泽显示404

flask run --port 3000

