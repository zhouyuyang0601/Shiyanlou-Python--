#coding=utf-8
"""
首先定义四个class,分别实例化然后在主函数中调用
    class(Args)
    class(Config)
    class(userdata)
    class(tax_calc)
"""
import sys
import csv
import os
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
    	tax_table_item(0, 0.03, 0)

#
# Real code begins here
#
class Args(object):
    def __init__(self):
        self.path = sys.argv[1:]

    def _parse_path(self):
        self.employee_dict={}
        for config in self.path:
            key,value=config.strip().split(',')
            try:
                self.employee_dict[key]=value
            except (IndexError,ValueError,TypeError):
                print('You entered wrong parameters')
                sys.exit()
        
    def get_para(self,config):
        try:
            return self.employee_dict[config]
        except ValueError:
            print(you required a wrong path)
            sys.exit()
#定义实例arg为Args类，方便在之后调用
arg=Args()

class Config(object):
    def __init__(self):
        self.config_path=arg('-c')

    def _parse_config(self):
        self.config_dict={}
        try:
            with open self.config_path as f:
                    for lines in f:
                       key,value=f.strip().split('=')
                       self.config_dict[key.strip()]='{:.2f}'.format(float(value.strip()))
        except (ValueError,IndexError,TypeError):
            print('Errors in config dict input')
            sys.exit()

    def get_para(self,para):
        try:
            return self.config_dict[para]
        except (ValueError):
            print('You entered a wrong config para')
            sys.exit()
    
    @property
    def shebao_L(self):
        return self.config_dict['JiShuL']
    def shebao_H(self):
        return self.config_dict['JiShuH']
    def total_rate(self):
        for para_value in self.config_dict.values():
            para_sum +=para_value
        para_sum -=self.config_dict['JiShuL']-self.config_dict['JiShuH']
        return para_sum

#定义一个config类的实例
config=Config()

class Userdata(object):
    def __init__(self):
        self.user_path=arg('d')
    
    def _parse_user_data(self):
        self.user_data_dict={}
        try:
            with open self.user_path as f:
                for employee in f:
                    user_id, salary=employee.strip().split(',')
                    self.user_data_dict[user.id.strip()]='{:.2f}'.format(float(salary.strip()))
        except(ValueError,IndexError):
            print('wrong userdata,check it ')
            sys.exit()

    def get_user(self,user_id):
        return self.user_data_dict[user_id]
    @property
    def all_user(self)：
        return self.user_data_dict

#定义一个user类的实例
user_data=Userdata()

class tax_calc(object):

    def __init__(self):
        self.userdata=user_data.all_user

    @staticmethod
    



    
