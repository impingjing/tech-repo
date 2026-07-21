shopping_list=["key","rat"] # 空列表 shopping_list=[]
#方法不同于函数 对象.方法() 函数(对象)
shopping_list.append("banana") #添加
print("After appending:",shopping_list)
shopping_list.remove("key") #删除
print("After removing:",shopping_list)
print(shopping_list[0]) #索引，支持随机访问

num_list=[1,5,3,2,6]
print(max(num_list)) #打印列表里的最大值
print(min(num_list)) #打印列表里的最小值
print(sum(num_list)) #打印列表中所有元素的和
print(num_list)
print("After sorting:")
print(sorted(num_list)) #打印排序好的列表（升序）

# 列表是可变的，但字符串、整数、浮点数和布尔类型都是不可变的
s="Hello"
print(s.upper()) #打印结果是HELLO
print(s) #依旧是 Hello