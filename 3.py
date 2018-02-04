#config: configs for different cities
#salary(csv): index:salary
#output(csv):index,salary_before_tax,insurance,tax,salary_after_tax

import os
import sys

#mlh 
class Args(object):
	def __init__(self):
		self.args = sys.argv[1:]

#config
class Config(object):
	def __init__(self):
		self.config=self._read_config()
	def _read_config(self):
		config={}

#user
class UserData(object):
	def __init__(self):
		self.userdata=self._read_users_data()
	def _read_users_data(self):
		userdata=[]

#tax
class IncomeTaxCalculator(object):
	#calculate function	
	def calc_for_all_userdata(self):

	#output csv function
	def export(self,default='csv'):
		result=self.calc_for_all_userdata()
		with open('////') as file:	
			write =csv.writer(f)
			write.writerows(result)

#execute
if __name__== '__main__':
	....
