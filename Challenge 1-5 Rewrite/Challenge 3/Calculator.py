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
    	tax_table_item(0, 0.03, 0)]

#
# Real code begins here
#
class Args(object):
    def __init__(self):
        self.path = sys.argv[1:]

    def get_para(self,config):
        try:
            return self.path[self.path.index(str(config))+1]
        except (ValueError):
            print('you required a wrong path')
            sys.exit()
#定义实例arg为Args类，方便在之后调用
arg=Args()

class Config(object):
    def __init__(self):
        self.config_path=arg.get_para('-c')

    def parse_config(self):
        config_dict={}
        try:
            with open(self.config_path) as f:
                    for lines in f:
                       key,value=lines.strip().split('=')
                       config_dict[key.strip()]='{:.2f}'.format(float(value.strip()))
        except (ValueError,IndexError,TypeError):
            print('Errors in config dict input')
            sys.exit()
        #print config_dict
        return config_dict

    def get_para(self,para):
        cfg_dict=self.parse_config()
        try:
            return cfg_dict[para]
        except (ValueError):
            print('You entered a wrong config para')
            sys.exit()
    
    @property
    def shebao_L(self):
        return self.get_para('JiShuL')
    @property    
    def shebao_H(self):
        return self.get_para('JiShuH')
    @property
    def total_rate(self):
        para_sum=0
        for para_value in self.parse_config().values():
            para_sum +=para_value
        para_sum -=self.shebao_L-self.shebao_H
        return para_sum

#定义一个config类的实例
config=Config()

class Userdata(object):
    def __init__(self):
        self.user_data=self._parse_user_data()
    
    def _parse_user_data(self):
        user_data=[]
        try:
            with open(arg.get_para('-d')) as f:
                for employee in f:
                    user_id, salary=employee.strip().split(',')
                    user_data.append([user_id,salary])
        except(ValueError,IndexError):
            print('wrong userdata,check it ')
            sys.exit()
        return user_data
    def __iter__(self):
        return iter(self.user_data)



class tax_calc(object):

    def __init__(self):
        self.userdata=Userdata()

    @staticmethod
    def shebao_judge(salary):
        try:
            salary=float(salary)
        except TypeError:
            print('Wrong type of value in shebao_judge')
            sys.exit()
        if salary<=config.shebao_L:
            shebao=config.shebao_L*config.total_rate
        if salary>=config.shebao_H:
            shebao=config.shebao_H*config.total_rate
        else:
            shebao=salary*config.total_rate
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
                tax =0 
                break
            elif salary_taxable>=i.salary_bound:
                tax='{:.2f}'.format(float(salary_taxable*i.rate-i.quick_subtractor))
                break        
    
        salary_left = '{:.2f}'.format(float(salary-shebao - float(tax)))
        newdata=[shebao,tax,salary_left]
        print(type(newdata))
        return new_data
    
    def calc_all_user(self):
        data=Userdata()
        for i in data:
            #print(i)
           # print(i[1])
            result=self.tax_calc(3500)
            print(result)
            i.extend(tax_calc(i[1]))
        return data
    
    #逐行打印列表
    def print_salary_table(self):
        with open (arg.get_para('-o'),'w') as file:
            writer=csv.writer(file)
            writer.writerows(self.calc_all_user())

if __name__=='__main__':
    calculator=tax_calc()
    calculator.print_salary_table()



    
