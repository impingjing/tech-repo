user_name=input("Please enter your name: ")
print("Welcome " + user_name)
# input一律返回字符串
user_age=input("Please enter your age: ")
print(user_age)
# user_age+10 会报错！
user_age=int(user_age)+10 #类型转换
print("After ten years: "+str(user_age)) #类型转换
# 注意：+只能用于字符串之间的拼接，而不能用于字符串和数字之间的拼接
print("After ten years: ",user_age) #不同类型之间用“,”