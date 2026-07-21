# f-strings 格式化字符串字面量
name="Amy"
age=19
# 直接插入变量
print(f"Hello, {name}! You're {age} years old.")
# 插入表达式
print(f"Next year, you will be {age + 1} years old.")
# 格式化控制：可以在 {} 中使用冒号 : 后跟格式说明符
pi=3.14159
print(f"Value of pi is {pi:.2f}") #保留两位小数

# str.format()方法
# 按顺序自动匹配
print("My name is {}, I am {} years old.".format(name,age))
# 按索引位置指定（可重复使用）
print("I love {0}, she loves {0} too.".format("Apple"))
print("I love {0}, you love {1}.".format("you","me"))
# 使用关键字参数（顺序可随意调换）
print("Name:{name},Age:{age}".format(age=20,name="Bob"))

# 格式化控制
#1.
# 居中对齐，总宽度为10，不足部分用 * 填充
print("{:*^10}".format(123)) #打印结果：***123****
print("{:^10}".format(123))  #打印结果：   123
# {:*<10} 左对齐 {:*>10} 右对齐
# 如果不表明对齐方式则默认为右对齐；如果不表明填充方式则默认空格填充
#2.
# 千位分隔符
print("{:,}".format(123456789))