#问题
数据库中需要包括 commits, branch ,releases的数量

#目标页面
https://github.com/shiyanlou?tab=repositories

#配置
sudo service mysql start
mysql > create databases shiyanlougithub;
python3 models.py
sudo pip3 mysqlclient sqlalchemy

#tips
1.仓库名称和更新信息从https://github.com/shiyanlou?tab=repositories 页面获取
2.其他的提交信息等需要从 https://github.com/shiyanlou/xxxx 这样的仓库页面获取并存储到数据库中的同一个表中
3.在处理时，页面的数字字符串有可能有这种形式 2,412，所以在转化成整数的时候需要去掉逗号
4.在settings.py中关闭robots

#修改
首先在Models.py中加入 commits, branches, releases等(integer)变量,执行文件，将表加入文件中
这个地方应该是用multipage的方法，进入页面提取：
commits= li 'commits 'num text-emphasized' commits
branches=li 'commits 'num text-emphasized' branch
releases=li 'commits 'num text-emphasized' releases

-start_url不做更改
-parse后加入repo_url，使用url_join补全链接，输出request(callback函数写成repo_parse),用request.meta('item')传递item
-新增repo_parse
    这一段写的时候有一点小trick，对于获取html,xml的链接的基本功还是得练习一下
    它这里有type_text和number_text两个变量来存储数字和类型，都放在<ul class 'numbers summary>




