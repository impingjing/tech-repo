#引入模块的三大方式
#1.import
import statistics
print(statistics.mean([1, 2, 3])) #数据的算术平均数
print(statistics.median([1, 2, 3])) #数据的中位数
#2.from+import 只引入特定函数
from math import sqrt,sin,cos
print(sqrt(2))
print(sin(2))
print(cos(2))
#3.from+import* 全部被引入
from statistics import*
print(mean([1, 2, 3]))
print(median([1, 2, 3]))

# control+click函数名
# pypi.org提供了很多有趣的第三方库（引入非官方库时，必须先安装pip install（去终端安装）后引用import）
