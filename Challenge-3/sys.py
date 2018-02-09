import sys
#use to validate the idea of sys.argv
class arg(object):
	def __init__(self):
		self.args=sys.argv[1:]
	def get_para(self,para):	
		try:
			self.para=para
		except ValueError:
			print('You entered a wrong parameter')
	def return_para(self):
		return self.para
	def return_path(self,para):
		self.para=para
		path= self.args[self.args.index(self.para)+1]
		return path
	

if __name__ == '__main__':
	test=arg()
	print(type(test))
	print(test.return_path('-c'))
	print('end')