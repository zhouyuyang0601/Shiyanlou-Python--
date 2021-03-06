#挑战3 

##文档
支持从配置文件中读取社保的税率，并读取员工工资数据 CSV 文件，同时将输出信息写入员工工资单 CSV 文件中。

计算器执行中包含下面的三个参数：

>-c 配置文件：由于各地的社保比例稍有不同，我们为每个城市提供一个社保比例的配置文件。
>-d 员工工资数据文件（CSV 格式）： 指定员工工资数据文件，文件中包含两列内容，分别为员工工号和工资金额。
>-o 员工工资单数据文件（CSV 格式）： 输出内容，将员工缴纳的社保、税前、税后工资等详细信息输出到文件中。

##要求
>用面向对象编程的方式编程，将计算封装在Class类中
    class(Args)
    class(Config)
    class(userdata)
    class(tax_calc)

>JiShuL 为社保缴费基数的下限，即工资低于 JiShuL 的值的时候，需要按照 JiShuL 的数值乘以缴费比例来缴纳社保。
>JiShuH 为社保缴费基数的上限，即工资高于 JiShuH 的值的时候，需要按照 JiShuH 的数值乘以缴费比例缴纳社保。
>当工资在 JiShuL 和 JiShuH 之间的时候，按照你实际的工资金额乘以缴费比例计算社保费用。

个税计算公式：

应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
应纳税额 = 应纳税所得额 × 税率 － 速算扣除数


##测试
./calculator.py -c /home/shiyanlou/test.cfg -d /home/shiyanlou/user.csv -o /tmp/gongzi.csv
在指定位置输出文件gongzi.csv

###在本地测试的代码
python "c:\Code\Shiyanlou-Python--\Week 1 Rewrite\Challenge 3\Calculator.py" '-c' 'c:\Code\Shiyanlou-Python--\Week 1 Rewrite\Challenge 3\test.cfg' '-d' 'c:\Code\Shiyanlou-Python--\Week 1 Rewrite\Challenge 3\user.csv' '-o' 'c:\Code\Shiyanlou-Python--\Week 1 Rewrite\Challenge 3\gongzi.csv'
###家里电脑
python "D:\Code\Shiyanlou-Python--\Week 1 Rewrite\Challenge 3\Calculator.py" '-c' 'D:\Code\Shiyanlou-Python--\Week 1 Rewrite\Challenge 3\test.cfg' '-d' 'D:\Code\Shiyanlou-Python--\Week 1 Rewrite\Challenge 3\user.csv' '-o' 'D:\Code\Shiyanlou-Python--\Week 1 Rewrite\Challenge 3\gongzi.csv'

>101,3500
203,5000
309,15000
###工号，税前工资，社保，税，税后工资
>101,3500,577.50,0.00,2922.50
203,5000,825.00,20.25,4154.75
309,15000,2475.00,1251.25,11273.75

>员工工资单数据文件，即本实验需要输出得到的数据文件。同样，输出的员工工资单数据文件中，每行格式为 
    工号,税前工资,社保金额,个税金额,税后工资

#知识点
面向对象编程

#感触
在最开始写code的时候，对于使用的变量类型思考清楚，会极大的降低后期改bug的麻烦

#真他妈是个Disaster
光是让代码的语法错误改完就花了我两个小时，更不用说错误的调用带来的肮脏的数据格式混乱
我重写一个只要30分钟，弄明白我昨天为什么这么想的，都改了起码2个小时
我真的应该认认真真的读一读手册

#关于类
我认为实验楼和Kaiser的课关于Class()讲的实在是很糟糕
我最开始认为self只是一个无关紧要的值，但是后续来看，我的理解全部错误了。
因此在最开始,也就是我改了很长时间的，这个重写了，我最后花了很长时间去一个个补漏
