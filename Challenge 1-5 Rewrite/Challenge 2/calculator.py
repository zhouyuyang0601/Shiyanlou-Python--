#coding=utf-8
"""
首先从命令行中读取输入信息
将信息从列表转换为字典
调用计算函数
计算函数应该扣除对应的社保费率
计算出每个工号对应的税后工资
分行输出每个工号的信息
"""
#定义所需的信息
from collections import namedtuple
import sys
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
]
Social_ins_rate= 0.165
"""
养老保险：8%
医疗保险：2%
失业保险：0.5%
工伤保险：0%
生育保险：0%
公积金：6%
"""

# Read from prompt
employee_list = sys.argv[1:]
#print(employee_list)
employee_dict={}

try:
    for i in employee_list:
        #print(i)
        employee_id,salary=i.split(':')
        #print(employee_id,salary)
        employee_dict[int(employee_id.strip())]='{:.2f}'.format(float(salary.strip())) 
except (ValueError,IndexError,TypeError):
    print('You Enter a Wrong user paramter,plz try again')
    sys.exit()

def calc(value):
    """
    1.应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
    2.应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
    在挑战2中社保为16.5%
    """
    salary=float(value)
    salary_taxable=salary-tax_start_point-salary*Social_ins_rate
    for i in tax_table:
        if salary<=tax_start_point:
            tax =0 
            break
        elif salary_taxable>=i.salary_bound:
            tax='{:.2f}'.format(float(salary_taxable*i.rate-i.quick_subtractor))
            break
    salary_left = '{:.2f}'.format(float(salary) - float(tax))
    return salary_left

output_dict=employee_dict

for employee in employee_dict:
    salary_after_tax= calc(employee_dict[employee])
    output_dict[employee]=salary_after_tax

#print result
for k,v in output_dict.items():
    print('{k}:{v}'.format(k= k, v = v))
