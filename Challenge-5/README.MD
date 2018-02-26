#文档
使用 getopt 模块处理命令行参数
使用 Python3 中的 configparser 模块读取配置文件
使用 datetime 模块写入工资单生成时间
计算器执行中包含下面的参数：

-h 或 --help，打印当前计算器的使用方法，内容为：
Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata
-C 城市名称 指定使用某个城市的社保配置信息，如果没有使用该参数，则使用配置文件中 [DEFAULT] 栏目中的数据，城市名称不区分大小写，比如配置文件中写的是 [CHENGDU]，这里参数可以写 -C Chengdu，仍然可以匹配
-c 配置文件 配置文件，由于各地的社保比例稍有不同，我们将多个城市的不同配置信息写入一个配置文件
-d 员工工资数据文件 指定员工工资数据文件，文件中包含两列内容，分别为员工工号和工资金额
-o 员工工资单数据文件 输出内容，将员工缴纳的社保、税前、税后工资等详细信息输出到文件中

#配置文件
[DEFAULT]
JiShuL = 2193.00
JiShuH = 16446.00
YangLao = 0.08
YiLiao = 0.02
ShiYe = 0.005
GongShang = 0
ShengYu = 0
GongJiJin = 0.06

[CHENGDU]
JiShuL = 2193.00
JiShuH = 16446.00
YangLao = 0.08
YiLiao = 0.02
ShiYe = 0.005
GongShang = 0
ShengYu = 0
GongJiJin = 0.06

[BEIJING]
JiShuL = 4251.00
JiShuH = 21258.00
YangLao = 0.08
YiLiao = 0.02
ShiYe = 0.002
GongShang = 0
ShengYu = 0
GongJiJin = 0.12

#工资数据
101,3500
203,5000
309,15000

#输出格式
输出的员工工资单数据文件每行格式为 工号,税前工资,社保金额,个税金额,税后工资,计算时间如下：

101,3500,577.50,0.00,2922.50,2017-09-01 10:02:00
203,5000,825.00,20.25,4154.75,2017-09-01 10:02:00
309,15000,2475.00,1251.25,11273.75,2017-09-01 10:02:00

#测试条件
calculator.py -C cityname -c configfile -d userdata -o resultdata
###家里电脑
python "D:\Code\Shiyanlou-Python--\Challenge 5\Calculator.py" '-c' 'D:\Code\Shiyanlou-Python--\Challenge 5\test.cfg' '-d' 'D:\Code\Shiyanlou-Python--\Challenge 5\user.csv' '-o' 'D:\Code\Shiyanlou-Python--\Challenge 5\gongzi.csv'

Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata
-h 或 --help，打印当前计算器的使用方法，内容为：
-C 城市名称 指定使用某个城市的社保配置信息，如果没有使用该参数，则使用配置文件中 [DEFAULT] 栏目中的数据，城市名称不区分大小写，比如配置文件中写的是 [CHENGDU]，这里参数可以写 -C Chengdu，仍然可以匹配
-c 配置文件 配置文件，由于各地的社保比例稍有不同，我们将多个城市的不同配置信息写入一个配置文件
-d 员工工资数据文件 指定员工工资数据文件，文件中包含两列内容，分别为员工工号和工资金额
-o 员工工资单数据文件 输出内容，将员工缴纳的社保、税前、税后工资等详细信息输出到文件中

#参考
基于 getopt 模块处理程序的参数
基于 configparser 实现配置文件的读取
基于 datetime 返回数据计算的时间
最后，如果你希望保存自己的程序，可以将代码提交到自己的 Github 账号中

#知识点
Python3 模块使用
getopt 处理命令行参数
configparser 读取配置文件
datetime 格式化输出时间

