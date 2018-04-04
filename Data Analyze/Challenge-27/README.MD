#目标
温室气体排放和气温变化的联系

# 世界银行气候变化数据集
wget http://labfile.oss.aliyuncs.com/courses/1013/week7/ClimateChange.xlsx

# NASA 全球温度变化数据集
wget http://labfile.oss.aliyuncs.com/courses/1013/week7/GlobalTemperature.xlsx

NASA 全球温度变化数据集只包含一个表，该表由 5 列组成，分别是：

Date：按月统计日期（从 1950 年 1 月至 2015 年 12 月）
Land Average Temperature：陆地平均温度
Land Max Temperature：陆地最高温度
Land Min Temperature：陆地最低温度
Land And Ocean Average Temperature：陆地-海洋平均温度

#效果
挑战需要依据提供的数据集得到地球历年的温室气体排放量及对应年份的地表或海洋平均温度，最后绘制出相互之间的关系图像。

挑战最后需要得到由 Matplotlib 绘制出的数据关系图像，且由 4 个子图组成，分别为：

子图 1（线形图）：绘制 1990 年 - 2010 年间，「全球历年温室气体排放总量」与「历年陆地平均温度」及「历年陆地-海洋平均温度」三者之间的线形图。
子图 2（柱状图）：绘制 1990 年 - 2010 年间，「全球历年温室气体排放总量」与「历年陆地平均温度」及「历年陆地-海洋平均温度」三者之间的柱状图。
子图 3（面积图）：绘制有气象数据的年份，「各季度地面平均温度」与「各季度地面-海洋平均温度」面积图。
子图 4（核密度估计图）：绘制有气象数据年份，「各季

#提示语
使用 pd.read_excel() 读取 Excel 文件，并使用 sheetname='表名' 参数指定不同的数据表，详见该方法的 参考文档。
使用 pandas.Series.fillna() 对缺失值按向前或向后的顺序近邻填充，参数 method='ffill' 表示按照前面一个值进行填充，method='bfill'表示按照后面一个值进行填充。还可以通过设定 axis=0 或 1 更改按列或行方向填充。本挑战中，某些行既需要向前填充，也需要向后填充才能补齐。题目约定先按照前面值填充，再按照后面值填充，即：DataFrame.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1) 完成。详见该方法的 参考文档。
使用 pandas.DataFrame.set_index() 可将某一列设为索引，详见该方法的 参考文档。
使用 pandas.DataFrame.dropna() 可以去掉包含空值的行，详见该方法的 参考文档。
可以使用 pd.to_datetime() 将数据处理成时间索引，详见该方法的 参考文档。
可以使用 DataFrame.resample() 对时间序列数据进行重新采样，详见该方法的 参考文档。
使用 pandas.concat() 可以合并 DataFrame，详见该方法的 参考文档。
你可以直接使用 pandas.DataFrame.plot() 对 DataFrame 数据绘图，通过设定 kind='' 参数绘制不同的图形。详见该方法的 参考文档。
Min-Max 标准化算法公式为：新数据 =（原数据-最小值）/（最大值-最小值），
按季度降采样，可以使用 Offset='Q' 参数。
你需要使用到 Matplotlib 中 subplot 子图绘制相关的知识。可以再次阅读上周的教学内容，或学习实验楼先前关于 Matplotlib 使用的相关课程。
测试时请使用 /home/shiyanlou/anaconda3/bin/python 运行 challenge7_3.py，避免出现找不到 Pandas 的情况。

#名称
名称约定
为了统一绘图样式，现约定相关名称如下。

子图 1 （左上）中：

绘图标题：自定义，可以不设置标题
横轴标题：Years
纵轴标题：Values
子图 2 （右上）中：

绘图标题：自定义，可以不设置标题
横轴标题：Years
纵轴标题：Values
子图 3 （左下）中：

绘图标题：自定义，可以不设置标题
横轴标题：Quarters
纵轴标题：Temperature
子图 4 （右下）中：

绘图标题：自定义，可以不设置标题
横轴标题：Values
纵轴标题：Values

