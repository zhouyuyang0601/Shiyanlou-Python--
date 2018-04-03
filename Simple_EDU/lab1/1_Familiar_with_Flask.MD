# 下载代码文件并解压
$ wget http://labfile.oss.aliyuncs.com/courses/923/week7/code/lab1.zip

#单独Flask App 的缺点
    Flask app + templates + statics 的小型静态页面不适合用于中大型的项目

#中大型项目
    后端代码模块化，将代码划分为多个文件。如果太大再拆分成多个文件，放在一个目录下

#页面模块化
    jinjia2的Block语法将网页划分成多个blcok,利用可以继承的特性，建立页面之间的相互继承的关系。

##知识点
    #Flask Web框架
    #后端模块化
    #前端模块化
    #blueprint
    #bootstrap

#后端模块化
    simpleedu/
        __init__.py
        config.py
        models.py
        forms.py
        app.py

    -Config.py 配置文件:python可以从一个python类中读取配置，那么可以用不同的类来写配置
                BaseConfig, DevelopmentConfig, ProductionConfig, TestingConfig
    -models.py 数据模型文件
                用于存储与数据库相关的信息
    
#config.py
    用于存储配置

#Bootstrap
    用Container的办法来存储一些东西