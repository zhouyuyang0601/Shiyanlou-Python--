#initiate
import sys
salary_dict={}
#input
try:
	for arg in sys.argv[1:]:
		salary_dict[int(arg.split(':')[0])]=int(arg.split(':')[1])
except ValueError:
	print('Parameter Error')
#
#Function
#
def tax_calc(salary):
	ins_rate=0.165
	taxinc=salary*(1-ins_rate)-3500
	if taxinc <=0:
		tax=0
	elif taxinc<=1500:
		tax=taxinc*0.03
	elif taxinc>1500 and taxinc<=4500:
		tax=taxinc*0.1-105
	elif taxinc>4500 and taxinc<=9000:
		tax=taxinc*0.2-555
	elif taxinc>9000 and taxinc<=35000:
		tax=taxinc*0.25-1005
	elif taxinc>35000 and taxinc<=55000:
		tax=taxinc*0.30-2755
	elif taxinc>55000 and taxinc<=80000:
		tax=taxinc*0.35-5505
	elif taxinc>=80000:
		tax=taxinc*0.45-13505
	salary_after_tax=salary*(1-ins_rate)-tax
#output
for index,salary in salary_dict.items():
	print('{}:{0:.2f}'.format(index,tax_calc(salary)))
