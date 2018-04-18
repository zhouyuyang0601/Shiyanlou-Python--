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