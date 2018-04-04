#Dataset
wget http://labfile.oss.aliyuncs.com/courses/764/user_study.json

#example
{"minutes": 30, "created_at": "2016-05-01 00:00:10", "user_id": 199071, "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406", "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"}

user_id 用户 ID
lab 实验名称
course 课程名称
minutes 学习分钟数
created_at 学习时间

#analysis function (self, para1, para2)
    para1=文件Json名字
    para2=User_id

        使用pandas读取json文件，统计指定ID的学次数和学习总分钟数
            return value 1, value2
        value1 制定用户的学习次数
        value2 制定用户的总学习时间

#tips
如果不存在，返回0 
pandas.read_json 来阅读json
DataFrame 使用筛选来选择出user_id==para2
使用3.6Python


