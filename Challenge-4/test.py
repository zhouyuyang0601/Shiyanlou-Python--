"""
fuck this shit
2.18.2018
use queue to communicate among processes
use Multiprocess to create 3 processes, each handles read, calc, print
启动三个进程，使用进程 1 读取员工工资数据，使用进程 2 计算个税及社保，使用进程 3 将数据写入到输出的工资单数据文件中。

实现方案可以考虑定义 queue1 和 queue2，实现三个进程如下：

进程 1：从用户文件中读取数据，然后得到一个列表 data，第一项是用户 ID，第二项是税前工资，然后使用 queue1.put(data)。
进程 2：queue1.get() 得到列表 data，第一项是用户 ID，第二项是税前工资，然后计算后生成新的列表。 newdata，包含社保，个税，税后工资等数据，然后使用 queue2.put(newdata)。
进程 3：queue2.get() 得到列表 newdata，包含用户 ID，税前工资，社保，个税，税后工资等数据，然后写入文件。
读取员工数据进程每读取一项员工数据就会将其放到队列 Q1 当中，
而计算税额进程则会从队列 Q1 中获取相应的员工数据项，然后计算税额，计算完成后将结果放到队列 Q2 中，
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
        输出进程
执行方式:
    python3 calculator_multiprocess.py  -c test.cfg -d user.csv -o gongzi.csv
"""

import sys
from collections import namedtuple
from multiprocessing import Process, Queue,Pool
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


#读取输入命令中的参数，-c 对应config -d 对应用户数据 -o 对应输出数据
class Args:
	def __init__(self):
		self.arg=sys.argv[1:]
		
	def _parse_arg(self,args):	
		try:
			return self.arg[self.arg.index(args)+1]
		except (ValueError,IndexError):	
			print('wrong args')

	def get_para(self,arg):
		try:
			return self._parse_arg(arg)	
		except (ValueError,KeyError):
			print('Dict does not contain it')


#定义配置文件读取
class Config(object):
	"""
	在这个中间，使用file文件进行传递参数
	Args:
		file(str)社保配置文件
	"""
	def __init__(self,file):	
		self.shebao_low, self.shebao_high, self.total_rate = self._read_config(file)

	def _read_config(self,file):	
		"""
		在多线程的模式下，我们从queue中读取所需要的文件信息
		"""
		#初始化值
		rate = 0
		shebao_low=0
		shebao_high=0

		#通过打开输入的file文件读取用户信息
		#不再使用字典格式存储数据
		with open(file) as f:	
			for lines in f:
				key,value= lines.strip().split('=')
				key=key.strio()
				try:
					value=float(value.strip())
				except ValueError:
					print('wrong config documents')
					exit()
				if key ==  'JiShuL'
					shebao_low = value
				if key == 'JiShuH'
					shebao_high = value
				else 
					rate += value
		"""
		因为是多线程调用，就不再在类中分开存储变量。
		在读取一行之后就传递值到计算线程中去
		所以直接在for lines的循环中判别
		"""
		return shebao_low,shebao_high,rate


class UserData(Process):
	#继承Process类
	#使用Run方法可以使得其像一个进程一样自动执行
	def __init__(self,file,output_queque):
		 """
        Args:
            file (str): 员工数据文件
            output_queue (object): multiprocessing.Queue 队列实例
        """
		self.file=file
		self.output_q=output_queque

		#重新initProcess
		super().__init__()
		
	def _parse(self):
		#解析员工数据，每次返回一行数据
		#yield函数是每次循环都返回一个数
		for line in open(self.file):
			employee_id, salary = line.split(',')
			yield (int(employee_id),int(salary))
	
	def run(self):
		"""
		进程启动后真正执行的方法
		将解析出的数据放在队列中
		"""
		for item in self.__parse()
			#item是每次解析出来的那列数据
			self.output_q.put(item)
		
class calc_tax(object):
	"""社保，个人所得税计算实现类
    计算方法:
    应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
    应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
    最终工资 = 工资金额 - 各项社会保险费 - 应纳税额
    个人所得税税率因应纳税所得额不同而不同，具体可以查询税率速查表得知。
    """
	def __init__(self,config,input_queue,out_queue):
		 """
        Args:
            config (object): SheBaoConfig 实例
            input_queue (object): 多进程队列，计算器将从这个队列中获取员工数据
            output_queue (object): 多进程队列，计算器将从计算结果放到这个队列中
        """
		self.config=config
		self.input_q=input_queue
		self.output_q=out_queue
		#init
		super().__init__()
	
	def calculate(self,data_item):
		"""
		data_item(tuple): 类似（100：5000）的（工号:工资）tuple
		"""
		employee_id,salary=data_item

		#计算社保
		if salary < self.config.shebao_low:
				shebao = self.config.shebao_low*self.config.total_rate
		elif salary > self.config.shebao_high:
				shebao = self.config.shebao_high*self.config.total_rate
		else:
			shebao = salary*self.config.total_rate
		
		#计算工资
		salary_left= salary- shebao
		tax_salary = salary_left - INCOME_TAX_START_POINT
			#阶梯计算
		if tax_salary < 0:
			tax=0
		else:
			for item in INCOME_TAX_QUICK_LOOKUP_TABLE
				if tax_salary>start_point:
					tax=tax_salary*tax_rate-quick_subtractor
					break
		# remain = salary - shebao - income tax
		remain_salary = salary_left - tax
		#返回员工ID，工资，社保，税，实发工资
		return str(employee_id), str(salary), '{:.2f}'.format(shebao), '{:.2f}'.format(tax), '{:.2f}'.format(salary_left)

		def run(self):
			while True:
				try:
					item= self.input_q.get(timeout=1)
				except queue.Empty:
					return
				#result
				result=self.calculate(item)
				self.output_q.put(result)
			
class Exporter(Process):
	def __init__(self,file,input_queue):
		"""
		file(str) 需要导出的文件
		input_queue(object):输入队列，从该队列导出所需的数据项
		"""
		self.file= open(file,'w')
		self.input_q = input_queue
		#init process
		super().__init__()

	def export(self,item):
		line = ','.join(item) +'\n'
		self.file.write(line)

	def run(self):
		while True:
			try:
				item=self.input_q.get(timeout=1)
			except queue.Empty:
				self.close 
				return
			self.export(item)


#excute
if __name__=='__main__':
	args=Args()
	config = Config(args.get_para('-c'))
	q1=Queue()
	q2=Queue()
	
	#三个进程

	# 员工数据进程
	userdata = UserData(args.get_para('-d',),q1)
	# 计算进程
	calculator = calc_tax(config,q1,q2)
	# 导出进程
	exporter = Exporter(args.get_para('-o'),q2)

	#启动进程
	userdata.start()
	calculator.start()
	exporter.start()

	#结束进程
	userdata.join()
	calculator.join()
	exporter.join()
	
		



