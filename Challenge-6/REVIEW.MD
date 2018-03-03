#文档
构建一个基于Flask框架的网站
网站可以访问两个本地json文件的内容：index路由；file路由
通过3000端口访问
自定义404 NOT FOUND页面
需要保证 http://localhost:3000/files/helloshiyanlou 可以访问到 /home/shiyanlou/files/helloshiyanlou.json 文件中的内容
需要保证 http://localhost:3000/files/helloworld 可以访问到 /home/shiyanlou/files/helloworld.json 文件中的内容

#测试
flask run -port 3000

#资源
wget http://labfile.oss.aliyuncs.com/courses/923/week2/helloshiyanlou.json
$ wget http://labfile.oss.aliyuncs.com/courses/923/week2/helloworld.json

#思路
@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示 `/home/shiyanlou/files/` 目录下所有 json 文件中的 `title` 信息列表
    

@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面

#提示
---Flask run -port 用于修改访问port
---index 路由实现中，需要使用 os 模块读取目标目录 /home/shiyanlou/files 下的 json 文件列表，然后将 json 文件使用上周学习的 json 序列化方式转成 Python 字典，最后使用 render_templates 函数使用字典对象生成页面。
    1.os模块读取json文件列表
    2.json序列化转为字典
    3.render_templates生成页面
---file 路由实现中，需要使用 os.path 模块查看目标目录 /home/shiyanlou/files 是否有 filename.json 文件，如果不存在则返回包含字符串 shiyanlou 404 的 404 页面，如果有则使用 json 序列化方式提取内容并使用 render_templates 展示到页面上。
    1.os.path查看目录
    2.是：序列化并提取渲染
    3.否：返回自定义404页面
注意需要按照先前学的自定义 Flask 404 页面

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

#html
<!DOCTYPE HTML> 指示了页面的文档类型是 HTML5 文档

<head></head>位于头部
    <meta> 元素可提供有关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。
    <meta> 标签位于文档的头部，不包含任何内容。<meta> 标签的属性定义了与文档相关联的名称/值对。
    charset用于定义字符接的类别，中文的是UTF-8
    <title></title>用于定义文章的标题
<body></body>位于中段
    <ul></ul>用于展示无序列表
    ｛%...%｝是可执行列 Jinja2 的语法
     <li></li> :<li> 标签定义了列表项目。<li> 标签可用在有序列表 (<ol>) 和无序列表 (<ul>) 中。
     <p>这是一个段落。</p>:标记了一个段落