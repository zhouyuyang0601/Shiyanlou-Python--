#coding=utf-8
"""
2018.2.25
在亚运村家中
"""
import os
import sys
import csv
import configparser
import queue
from datetime import datetime
from multiprocessing import Process, Queue
from getopt import getopt, GetoptError
from collections import namedtuple

tax_start_point=3500.00
tax_table_item = namedtuple('tax_table_item',['salary_bound','rate','quick_subtractor'])
tax_table=[
    	tax_table_item(80000, 0.45, 13505),
    	tax_table_item(55000, 0.35, 5505),
    	tax_table_item(35000, 0.30, 2755),
    	tax_table_item(9000, 0.25, 1005),
    	tax_table_item(4500, 0.2, 555),
    	tax_table_item(1500, 0.1, 105),
    	tax_table_item(0, 0.03, 0)]

#
# Real code begins here
#

q_user = Queue()
q_result = Queue()

"""
首先定义四个class,分别实例化然后在主函数中调用
    class(Args)
    class(Config)
    class(userdata)
    class(tax_calc)
"""

class Args:
    
    def __init__(self):
        self.arg=sys.argv[1:]
        self.option=self._options()	
    def _options(self):
        try:
            path_list,_=getopt(self.arg,'-c:-d:-o:-h:',['help'])
        except (ValueError,GetoptError):
            print('you required a wrong path')
            sys.exit()
        #讲原先读入的List格式转为dict形式的字典
        options=dict(path_list)
        if len(options) == 1 and ('-h' in options or '--help' in options):
            print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
            exit()
        return options
    def _value_after_option(self,option):
        #使用get方式访问字典
        #self.option是通过调用_option()函数读来的
        #讲输入的值倒进去
        try:
            value=self.option.get(option)
        except (ValueError):
            print('Check you input')
            sys.exit()
        if value is None and option !='-C':
            print ('Parameter Error')
            sys.exit()
        return value
    #定义几个property
    @property
    def city(self):
        return self._value_after_option('-C')

    @property
    def config_path(self):
        return self._value_after_option('-c')

    @property
    def userdata_path(self):
        return self._value_after_option('-d')

    @property
    def export_path(self):
        return self._value_after_option('-o')


# define Variable Arg belongs to Args Class

args=Args()

class Config:

    def __init__(self):
        self.config=self._parse_config()
    
    def _parse_config(self):
        config = configparser.ConfigParser()
        config.read(args.config_path)
        #这个纯粹是题目本身的Bug
        #如果读取的东西是里面标出的，就切换到对应所在的城市
        if args.city and args.city.upper() in config.sections():
            return config[args.city.upper()]
        else:
            return config['DEFAULT']
    
    def return_config(self,para):
        try:
            return float(self.config.get(str(para)))
        except (ValueError,KeyError):
            print('Parameter Error')
            sys.exit()
    
    @property
    def shebao_H(self):
        return self.return_config('JiShuH')
    @property
    def shebao_L(self):
        return self.return_config('JiShuL')
    @property
    def total_rate(self):
        rate=0.00
        cfg_dict=self._parse_config()
        for items in cfg_dict.values():
            if float(items)<1.00:
                rate +=float(items)
        return rate
    
config=Config()

class User_Data(Process):

    def _parse_data(self):
        with open(args.userdata_path) as f:
            for lines in f.readlines():
                user_id, salary=lines.strip().split(',')
                try:
                    user_id=int(user_id)
                    salary=int(salary)
                except (ValueError,IndexError):
                    print('Problems in reading user data file')
                    sys.exit()
                yield (user_id,salary)
    
    def run(self):
        for data in self._parse_data():
            q_user.put(data)


class tax_calc(Process):
    def __init__(self):
        self.user=User_Data()
    
    @staticmethod
    def shebao_judge(salary):
        try:
            salary=float(salary)
        except TypeError:
            print('Wrong type of value in shebao_judge')
            sys.exit()
    
        if salary<=config.shebao_L:
            shebao=float(config.shebao_L)*float(config.total_rate)
        if salary>=config.shebao_H:
            shebao=float(config.shebao_H*config.total_rate)
        else:
            shebao=float(salary*config.total_rate)
        return shebao
    @classmethod
    def tax_calc(cls,salary):
        try:
            salary=float(salary)
        except TypeError:
            print('Wrong type of value in tax_calc')
            sys.exit()

        #调用静态函数计算社保    
        shebao=cls.shebao_judge(salary)
        #使用函数查询表来计算应缴税工资总数
        salary_taxable= salary-shebao
        #计算税金和税后工资
        for i in tax_table:
            if salary<=tax_start_point:
                tax =float(0.00)
                break
            elif salary_taxable>=i.salary_bound:
                tax=float(salary_taxable*i.rate-i.quick_subtractor)
                break        
        salary_left = float(salary-shebao-tax)
        newdata=['{:.2f}'.format(shebao),'{:.2f}'.format(tax),'{:.2f}'.format(salary_left)]
        return newdata
    
    def calc_all_user(self):
        while True:
            try:
                user_id,salary=q_user.get(timeout=1)
            except queue.Empty:
                return
            data=[user_id,salary]
            shebao='{:.2f}'.format(self.shebao_judge(salary))
            shebao,tax,remain=self.tax_calc(salary)
            data.extend((shebao,tax,remain))
            data.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            yield data
    def run(self):
        for data in self.calc_all_user():
            q_result.put(data)

class print_salary_table(Process):
    def run(self):
        with open (args.export_path,'w', newline='') as file:
             while True:
                writer = csv.writer(file)
                try:
                    item = q_result.get(timeout=1)
                except queue.Empty:
                    return
                writer.writerow(item)

if __name__=='__main__':
    workers = [
        User_Data(),
        tax_calc(),
        print_salary_table()
    ]
    for worker in workers:
        worker.run()

    





        