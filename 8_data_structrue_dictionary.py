#字典用于存储键值对
#contacts={} #空字典
contacts={"Amy":"123","Bob":"456","Charlie":"789"}
#注意：键的类型是不可变的(列表不能作为键)
contacts["Charlie"]="666"
print(contacts)

#元组不可变
example_tuple=("Amy","Bob","Charlie")
print(example_tuple)
#example_tuple.append("Jake") ❌️
#example_tuple.remove("Bob") ❌️

#利用元组可以实现同时存入相同名字不同年纪的数据
contacts_pro={("Amy",12):"123",("Amy",19):"456"}
print(contacts_pro)
print(contacts_pro[("Amy",12)])

#检查键是否存在
print("Charlie" in contacts)
print("Jake" in contacts)

#删除键值对
del contacts["Amy"] #如果键不存在则报错

#有多少键值对？
print(len(contacts))