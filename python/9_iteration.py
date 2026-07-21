"""
for 变量名 in 可迭代对象:
    对每个变量做一些事情
    ……
"""
temperature_dict={"011":36.5,"012":37.3,"013":36.2,"014":38.2}
temperature_dict.keys() #所有键
temperature_dict.values() #所有值
temperature_dict.items() #所有键值对

for staff_id,temperature in temperature_dict.items():
    if temperature >= 37:
        print("Run a fever:",staff_id) #找出所有发烧员工的工号

#for与range的结合
for i in range(5,10,2):
    print(i)
#range(起始，终止，步长) 步长默认为1，range序列不包括终止数

#计算从1到100的和
total=0
for i in range(1,101):
    total+=i
print(total)