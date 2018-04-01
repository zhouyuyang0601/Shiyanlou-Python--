#挑战一
##文档
个税计算公式：

应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
应纳税额 = 应纳税所得额 × 税率 － 速算扣除数

在挑战一中社保为0 

1.用命令行输入参数
calculator.py 3500
0.00
输出值为带有两位小数的值

2.遇到参数错误
输出('Parameter Error)

##知识点
Python3 程序开发
变量与数据类型 {:.2f}.format(float(value))
输出  print函数
命令行参数 (sys.argv[])来读取各种参数
运算  basic calculation
字符串 string.split
控制结构    换行
异常处理    try： except:

##总结
第一次写的时候对于sys.argv()的调用机制不太明白
异常处理中抛出错误和错误信息不太清楚
如果注释中有中文，需要在开头标出 #coding=utf-8
在计算完tax之后，记得及时break推出循环
报错后如果想结束程序，使用sys.exit()