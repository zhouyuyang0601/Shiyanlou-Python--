"""
fuck this shit
"""

import sys
import os
import csv
from collections import namedtuple
#
INCOME_TAX_START_POINT = 3500
IncomeTaxQuickLookupItem = namedtuple(
	'IncomeTaxQuickLookupItem',
	['start_point', 'tax_rate', 'quick_subtractor']
)
INCOME_TAX_QUICK_LOOKUP_TABLE = [
    	IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    	IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    	IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    	IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    	IncomeTaxQuickLookupItem(4500, 0.2, 555),
    	IncomeTaxQuickLookupItem(1500, 0.1, 105),
    	IncomeTaxQuickLookupItem(0, 0.03, 0)
]
#class 
class Args:
	def __init__(self):
		self.arg=sys.argv[1:]
		
	def _parse_arg(self,args):	
		try:
			return self.arg[self.arg.index(args)+1]
		except (ValueError,IndexError):	
			print('wrong args')
	def return_para(self,para):
		try:
			return self._parse_arg(para)	
		except (ValueError,KeyError):
			print('Dict does not contain it')
# define Variable Arg belongs to Args Class

args=Args()

#define Config Class
class Config(object):
	def __init__(self):	
		self.config=self._read_config()
	def _read_config(self):	
		#read path from Args class variable args	
		self.path=args.return_para('-c')
		#initialization
		config={}
		#open path 
		with open(self.path) as file:	
			for lines in file:
				key,value= lines.strip().split('=')
				try:
					config[key.strip()]=float(value.strip())
				except (ValueError, IndexError):
					print('wrong config documents')
					exit()
		return config
		
	def _get_config(self,key):
		try:
			return self.config[key]
		except KeyError:
			print('Config Error')
			exit()
	@property
	def shebao_low(self):
		return self._get_config('JiShuL')
	@property
	def shebao_high(self):
		return self._get_config('JiShuH')
	@property
	def total_rate(self):
		return sum([
			self._get_config('YangLao'),
			self._get_config('YiLiao'),
			self._get_config('ShiYe'),
			self._get_config('GongShang'),
			self._get_config('ShengYu'),
			self._get_config('GongJiJin')
			])
config=Config()

class UserData(object):
	def __init__(self):
		self.userdata=self._read_users_data()
		#inside function, read configs
	def _read_users_data(self):
		user_data_path=args.return_para('-d')
		user_data=[]
		with open(user_data_path) as file:
			for lines in file.readlines():
				employee_id, income_str=lines.strip().split(',')
				try:
					income=int(income_str)
				except ValueError:
					print('wrong userdata')
					exit()
	#convert each to data list
				user_data.append((employee_id,income))
		return user_data
	def __iter__(self):
		return iter(self.userdata)

class calc_tax(object):
	def __init__(self,userdata):
		self.userdata=userdata
	@staticmethod 
	def calc_shebao(income):
		#judge upper limit or lower limit
		if income<config.shebao_low:
			return config.shebao_low*config.total_rate
		if income>config.shebao_high:
			return config.shebao_high *config.total_rate
		return income*config.total_rate
	@classmethod
	def calc_tax_and_remain(cls,income):
		shebao = cls.calc_shebao(income)
		income_after_shebao=income-shebao
		income_taxable=income_after_shebao-3500
		#judge 
		if income_taxable<=0:
			return '0.00','{:.2f}'.format(income_after_shebao)
		for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
			if income_taxable>item.start_point:
				tax= income_taxable*item.tax_rate-item.quick_subtractor
				return '{:.2f}'.format(tax), '{:.2f}'.format(income_after_shebao -tax)
				
	#all user_data
	def calc_all_users(self):
		result=[]
		#iter to get all
		for employee_id,income in self.userdata:
			data=[employee_id,income]
			shebao='{:.2f}'.format(self.calc_shebao(income))
			tax,remain=self.calc_tax_and_remain(income)
			data += [shebao,tax,remain]
			result.append(data)
		return result
	def export(self,file_type='csv'):
		result = self.calc_all_users()
		with open(args.return_para('-o'),'w',newline='') as file:
			writer = csv.writer(file)
			writer.writerows(result)
			
if __name__=='__main__':
	calculator = calc_tax(UserData())
	calculator.export()
			
		
#excute


