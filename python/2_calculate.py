"""
计算优先级
() 乘方 */ +-
"""
import math #导入math库
print(math.sin(math.pi/2))
print(math.log2(8))

#一元二次方程根
a=-1
b=-2
c=3
x1=(-b+math.sqrt(b*b-4*a*c))/(2*a) #x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
print("x1=",x1)
print("x2=",x2)
