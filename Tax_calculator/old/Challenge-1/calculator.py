#coding=utf-8
"""
首先定义一个速算扣除表
根据工资的范围，使用循环结构去计算所属的税率和速算扣除数
"""
from collections import namedtuple
import sys
tax_start_point=3500
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

# Read salary from sys.argv
try:
    salary=float(sys.argv[1])
except (ValueError,TypeError):
    print("Parameter Error")
    sys.exit()

# run the calculator
"""
1.应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
2.应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
在挑战1中社保为0
"""
salary_taxable=salary-tax_start_point
for i in tax_table:
    if salary<=tax_start_point:
        tax =0 
        break
    elif salary_taxable>=i.salary_bound:
        tax='{:.2f}'.format(salary_taxable*i.rate-i.quick_subtractor)
        break

print(tax)
