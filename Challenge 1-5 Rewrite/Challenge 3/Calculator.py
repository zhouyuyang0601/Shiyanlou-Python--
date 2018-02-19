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
    
