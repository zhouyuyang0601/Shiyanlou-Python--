#文档
构建一个基于Flask框架的网站
网站可以访问两个本地json文件的内容：index路由；file路由
通过3000端口访问
自定义404 NOT FOUND页面
需要保证 http://localhost:3000/files/helloshiyanlou 可以访问到 /home/shiyanlou/files/helloshiyanlou.json 文件中的内容
需要保证 http://localhost:3000/files/helloworld 可以访问到 /home/shiyanlou/files/helloworld.json 文件中的内容


#提示
Flask run -port 用于修改访问port

#知识点
Flask 基本使用
Flask 自定义错误页面
注册路由
模板渲染
Jinja 语法
Jinja 继承
HTML 语法
CSS 语法
JSON 序列化
os 模
