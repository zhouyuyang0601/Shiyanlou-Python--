#文档
本次的挑战是使用进程来处理工资计算器
在数据量较大的情况下，我们希望提高计算效率。
通过三个进程，一个读取用户信息，一个计算税、社保和税后工资，一个写入到输出文件中
进程之间的通信可以使用Multiprocessing中的pipe或者Queue

#测试
./calculator.py -c test.cfg -d user.csv -o gongzi.csv

#实现思路
实现方案可以考虑定义 queue1 和 queue2，实现三个进程如下：

进程 1：从用户文件中读取数据，然后得到一个列表 data，第一项是用户 ID，第二项是税前工资，然后使用 queue1.put(data)。
进程 2：queue1.get() 得到列表 data，第一项是用户 ID，第二项是税前工资，然后计算后生成新的列表。 newdata，包含社保，个税，税后工资等数据，然后使用 queue2.put(newdata)。
进程 3：queue2.get() 得到列表 newdata，包含用户 ID，税前工资，社保，个税，税后工资等数据，然后写入文件。

#感想
其实就是把读取用户数据，计算这两个Class的继承对象改成了Process，
在操作时，按行读取 'readlines()' 读取文件中的数据，利用q_user.put推送出去
在tax_calc时，用q_user.get读取进来
计算出去的结果用q_result.put推送，在新建的~~以前的tax_cal类下exporter函数~~类中读取进来，再按行写入

在执行区域，每个进程用process()标定，用.run来运行

在计算时用timeout来将不活跃的进程结束

