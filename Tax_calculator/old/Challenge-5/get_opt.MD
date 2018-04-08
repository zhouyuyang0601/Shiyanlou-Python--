#文档说明
在挑战5中，使用get_opt读取命令行中的参数
http://python.usyiyi.cn/translate/python_352/library/getopt.html#module-getopt 中文文档
https://docs.python.org/2/library/getopt.html 英文文档

#内容
getopt.getopt(args, shortopts, longopts=[])
解析命令行选项和参数列表。args是要解析的参数列表，没有对正在运行的程序的引用引用。通常，这意味着sys.argv[1:]。
shortopts是脚本想要识别的选项字母的字符串，选项需要一个参数后跟一个冒号（':' getopt()使用）。
Longopts(可选)是用于支持长选项，在之前应该写上 --，在之后要跟上=

#实例
>>> import getopt
>>> args = '-a -b -cfoo -d bar a1 a2'.split()
>>> args
['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']
>>> optlist, args = getopt.getopt(args, 'abc:d:')
>>> optlist
[('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]
>>> args
['a1', 'a2']