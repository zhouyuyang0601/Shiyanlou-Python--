<<<<<<< HEAD
#coding=utf-8
"""
2018.2.24
于中石化SEI写下这行代码
读取员工数据进程每读取一项员工数据就会将其放到队列 Q1 当中，而计算税额进程则会
从队列 Q1 中获取相应的员工数据项，然后计算税额，计算完成后将结果放到队列 Q2 中，
输出进程则从 Q2 进程中获取计算结果，并将结果输出到文件当中。工作流程图如下:
    读取员工数据进程
          ||
          \/
        队列 Q1
          ||
          \/
      税额计算进程
          ||
          \/
        队列 Q2
          ||
          \/
        输出进程s
"""
import csv
import sys
from multiprocessing import Process
import Queue
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
"""
先定义几个queque队列
"""

q_user=Queue.Queue()
q_result=Queue.Queue()

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
    def return_para(self,para):
        try:
            index=self.arg.index(para)
            return self.arg[index+1]
        except (ValueError):
            print('you required a wrong path')
            sys.exit()
# define Variable Arg belongs to Args Class

arg=Args()

class Config:

    def __init__(self):
        self.path=arg.return_para('-c')
    
    def _parse_config(self):
        config_dict={}
        try:
            with open(self.path) as f:
                for lines in f:
                    keyword,values=lines.strip().split('=')
                    config_dict[keyword.strip()]=float(values.strip())
        except (ValueError,TypeError,AttributeError):
            print('you entered a wrong config document')
            sys.exit()
        return config_dict
    
    def return_config(self,para):
        cfg_dict=self._parse_config()
        try:
            return cfg_dict[str(para)]
        except (ValueError):
            print('You entered a wrong Value')
    
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
            if items<1.00:
                rate +=items
        return rate
    
config=Config()

class User_Data(Process):
    def __init__(self):
        self.path=arg.return_para('-d')
        self.data=self._parse_data()
    
    def _parse_data(self):
        with open(self.path) as f:
            for lines in f.readlines():
                user_id, salary=lines.strip().split(',')
        yield (user_id,int(salary))
    
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
        newdata=[shebao,tax,salary_left]
        return newdata
    
    def calc_all_user(self):
        while True:
            try:
                employee_id,income=q_user.get(timeout=1)
            except Queue.Empty:
                return
            data=[employee_id,income]
            result=self.tax_calc(data[1])
            user_list=list(data)
            output_list=[]
            output_list.append(user_list+result)
            return output_list
    
    def run(self):
        for data in self.calc_all_user():
            q_result.put(data)

class Exporter(Process):
    #逐行打印列表
    def run(self):
        with open (arg.return_para('-o'),'w') as file:
            while True:
                writer=csv.writer(file)
            try:
                item=q_result.get(timeout=1)
            except Queue.Empty:
                return
            writer.writerow(item)

if __name__=='__main__':
    worker =[
        User_Data(),
        tax_calc(),
        Exporter()]
    for work_process in worker:
        work_process.run()

    





        
=======
>>>>>>> e5d45fe64eec4268e8fc9da027aef67850ff577d
