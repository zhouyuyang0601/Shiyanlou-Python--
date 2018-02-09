# -*- coding: utf-8 -*-
import sys
import csv # 用于写入 csv 文件


# 处理命令行参数类
class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]

    """
    补充代码：
    1. 补充参数读取函数，并返回相应的路径.
    2. 当参数格式出错时，抛出异常.
    """

# 配置文件类
class Config(object):

    def __init__(self):
        self.config = self._read_config()

    # 配置文件读取内部函数
    def _read_config(self):
        config = {}

        """
        补充代码：
        1. 根据参数指定的配置文件路径，读取配置文件信息，并写入到 config 字典中.
        2. 使用 strip() 和 split() 对读取到的配置文件去掉空格以及切分.
        3. 当格式出错时，抛出异常.
        """

# 用户数据类
class UserData(object):

    def __init__(self):
        self.userdata = self._read_users_data()

    # 用户数据读取内部函数
    def _read_users_data(self):
        userdata = []

        """
        补充代码：
        1. 根据参数指定的工资文件路径，读取员工 ID 和工资数据.
        2. 可将员工工号和工资数据设置为元组，并存入 userdata 列表中.
        3. 当格式出错时，抛出异常.
        """

# 税后工资计算类
class IncomeTaxCalculator(object):

    # 计算每位员工的税后工资函数
    def calc_for_all_userdata(self):

        """
        补充代码：
        1. 计算每位员工的税后工资（扣减个税和社保）.
        2. 注意社保基数的判断.
        3. 将每位员工的税后工资按指定格式返回.
        """

    # 输出 CSV 文件函数
    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open("输出文件的路径，由输入参数获得") as f:
            writer = csv.writer(f)
            writer.writerows(result)


# 执行
if __name__ == '__main__':
    """
    按实际情况补充代码
	"""