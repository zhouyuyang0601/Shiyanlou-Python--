#各国历年二氧化碳排放量统计分析
考察Pandas模块的运用
    *读写数据
    *合并数据
    *归类数据
    *补齐缺失数据
        #补充Numpy和Pandas的相关课程
#GDP与二氧化碳排放量关联
    *考察Matplotlib
    *Min-Max标准算法
#温室气体与气温变化关联图
    *Matplotlib绘制子图
#地表温度预测
    *scikit-learn预测模块
        #scikit-learn的非监督学习和监督学习


##数据来源
wget http://labfile.oss.aliyuncs.com/courses/1013/week7/ClimateChange.xlsx

##目标
通过3个数据进行关联分析，得到 Income gourp Series Code 总量
各群体排放量最高和最低的国家及相应的排放量

##结果
如wm.jpg所示的DataFrame
Sum emissions 表示相应收入群体（Income group）的总排放量
Highest emission country 为相应收入群体里排放量最高的国家名称（Country name）。
Highest emissions 为排放量最高的国家对应的排放量数值。
Lowest emission country 为相应收入群体里排放量最低的国家名称。
Lowest emissions 为排放量最低的国家对应的排放量数值。

##要求
需要将代码保存到 Code 文件夹中，并以 challenge7_1.py 命名。
需要将最终返回 DataFrame 的代码写在 def co2() 中，不能修改函数名。
不能修改最终 DataFrame 的列名称和对应的索引名称，以上方结果示意图为参考。
你需要对有缺失值的年份数据进行填充，挑战规定使用#近邻数据#填充。
挑战不统计原始数据全部缺失的国家，也就是排放量最低的国家对应的排放量数值#不会为 0#

#---------------------------------------------------------------------------#
数据集解释

Data表：按国家，分年度统计的气候变化类资料
    -country Code: 国家代码
    -country name: 国家名称
    -series code:  数据类别代码
    -series name:  数据类别名称
    -统计数据
Country: 
    -Country Code:国家代码
    -Country Name；国家名称
    -Capital City：国家首都
    -Region:       国家所在区域
    -Income Group: 国家收入群体划分
    -Lending Cate: 世界银行借款类别
Series:
    -Data对应数据简介，代号 （挑战25中没有作用）

#麻烦一：如何读取excel
pandas内置的read_excel需要exlr包进行支持
sheet_name 用于区别不同的sheet
我希望把包保存在不同的dataframe里这样可能会更好的进行关联，然后再组合成一个整表
Ans:非常简单，阅读文档后发现通过sheet_name这个可以控制读什么

#麻烦二：如何根据标签进行分组：
已知二氧化碳排放量的标签是： EN.ATM.CO2E.KT，先把每年的二氧化碳排放累积求和
然后根据df_country里不同国家的income group进行区分
