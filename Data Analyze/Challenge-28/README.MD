#使用Scikit-learn来预测气温的变化趋势

    # 地球历年地表气温数据集
    wget http://labfile.oss.aliyuncs.com/courses/1013/week7/GlobalSurfaceTemperature.csv
    包含了 1850 年到 2010 年期间，地球地表的最高（Upper）、最低（Lower）以及中位数（Median）气温值

    # 地球历年温室气体排放数据集
    wget http://labfile.oss.aliyuncs.com/courses/1013/week7/GreenhouseGas.csv
    包含了 1960 年至 2013 年期间，地球历年温室气体排放量数据。

    # 地球历年大气 CO2 浓度数据集
    wget http://labfile.oss.aliyuncs.com/courses/1013/week7/CO2ppm.csv
    由 NASA 监测的 1980 年至 2016 年期间，地球大气中 CO2 平均浓度的数据

#3 个列表返回，并依次按照 最高、中位数以及最低气温 顺序
#保留3位小数
#最终预测 2011 年至 2017 的气温 ，平均绝对误差不超过 0.1 摄氏度。你无法看到 2011 年至 2017 年间的真实数据，系统判断时会自动将你的预测结果与 2011 年至 2017 年间监测的真实数据进行对比得到平均绝对误差。

使用 pd.read_csv() 读取 CSV 文件。
使用 pandas.Series.fillna() 对缺失值进行填充，详见该方法的 参考文档。或使用 pandas.DataFrame.interpolate 对缺失值进行数据拟合填充，详见该方法的 参考文档。
使用 pandas.DataFrame.set_index() 可将某一列设为索引，详见该方法的 参考文档。
可以使用 pd.to_datetime() 将数据处理成时间索引，详见该方法的 参考文档。
使用 pandas.concat() 可以合并 DataFrame，详见该方法的 参考文档。
测试时请使用 /home/shiyanlou/anaconda3/bin/python 运行 challenge7_4.py，避免出现找不到 Pandas 等模块的情况。
使用 from sklearn.metrics import mean_absolute_error 导入 mean_absolute_error 函数，可以快速验证平均绝对误差。
你可能需要使用到 sklearn 各模型提供的 fit() 方法训练模型，以及 predict() 方法用于预测。
你可以选择的 sklearn 用于回归预测的模型有线性回归（LinearRegression），随机森林回归（RandomForestRegressor），支持向量机回归（SVR）等。完成列表参见 官方文档。
