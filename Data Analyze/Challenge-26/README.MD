挑战内容是使用 Pandas 统计各国历年二氧化碳排放总量以及 GDP 的总量，最终通过 Matplotlib 绘制 各国 CO2 总量 与对应 GDP 总量 的关系曲线图。其中：

GDP 数值的 Series code 为：NY.GDP.MKTP.CD
CO2 排放数值的 Series code 为：EN.ATM.CO2E.KT

Challenge7_2.py 

def co2_gdp_plot()

某国家对应的数据全部缺失时，即没有相邻数据用于参考，那么使用 0 进行填充

CO2 总量 与 GDP 总量 在数值上差距悬殊，为了保证绘制到同一张图时具有良好的观赏性，必须针对两类数据进行归一化处理。挑战 规定必须使用 Min-Max 标准化算法对绘图数据进行归一化处理，算法公式详见提示语

plt.subplot() plt.show()
中国 Min-Max 归一化后的 CO2 和 GDP 数据(保留 3 位小数) 作为列表返回


####
提示语：
使用 pd.read_excel() 读取 Excel 文件，并使用 sheetname='表名' 参数指定不同的数据表，详见该方法的 参考文档。
使用 pandas.Series.fillna() 对缺失值按向前或向后的顺序近邻填充，参数 method='ffill' 表示按照前面一个值进行填充，method='bfill'表示按照后面一个值进行填充。还可以通过设定 axis=0 或 1 更改按列或行方向填充。本挑战中，某些行既需要向前填充，也需要向后填充才能补齐。题目约定先按照前面值填充，再按照后面值填充，即：DataFrame.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1) 完成。详见该方法的 参考文档。
使用 pandas.DataFrame.set_index() 可将某一列设为索引，详见该方法的 参考文档。
使用 pandas.DataFrame.dropna() 可以去掉包含空值的行，详见该方法的 参考文档。
使用 pandas.DataFrame.groupby() 可将数据安装某些类别归类，详见该方法的 参考文档。
使用 pandas.concat() 可以合并 DataFrame，详见该方法的 参考文档。
联合国安理会五大常任理事国中、美、英、法、俄对应的国家代码依次为：['CHN', 'USA', 'GBR', 'FRA','RUS']。
更多内容可参考 Pandas 完整官方文档（PDF）。并广泛利用像 Stackoverflow 等工具。
Min-Max 标准化算法公式为：新数据 =（原数据-最小值）/（最大值-最小值），即：X^{*}=\frac{X-X_{min}}{X_{max}-X_{min}}X
​​ 
关于 Min-Max 标准化，可利用搜索引擎了解，或阅读 相关文章。
测试时请使用 /home/shiyanlou/anaconda3/bin/python 运行 challenge7_2.py，避免出现找不到 Pandas 的情况。
