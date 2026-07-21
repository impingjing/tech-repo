def add(a,b):
    return a+b
#在函数中定义的变量都是局部变量，出了函数就不能被访问到
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
# 函数可以传入函数，称为高阶函数
# 函数作为另一个函数参数时，不能加()
def calculate_print(num1,num2,calculator):
    result=calculator(num1,num2)
    print(f"""
    | 数字参数 | {num1} | {num2} |
    | 计算结果 | {result} |""")

calculate_print(2,3,add)
calculate_print(2,3,subtract)
calculate_print(2,3,multiply)
calculate_print(2,3,divide)

# 匿名函数 Lambda
calculate_print(2,3,lambda a,b: a>b)
# (lambda a,b:a+b)(2,3)