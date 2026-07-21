"""
异常类型
1.
number_list = [1,2,3,4,5,6,7,8,9]
number_list[9]  # IndexError
2.
print(2/(12-15+3)) # ZeroDivisionError
3.
f=open("./test.txt","r") # FileNotFoundError
4.
"yoo"*"hey" # TypeError
"""

try:
    user_weight=float(input("Please enter your weight (kg):"))
    user_height=float(input("Please enter your height (m):"))
    user_bmi=user_weight/user_height**2
# except语句按顺序执行，若第一个异常被找到，则不会再找其他异常
except ZeroDivisionError:
    print("Height is zero")
except ValueError:
    print("Value is invalid")
except:
    print("Something is wrong")
else: # 如果程序没有异常，则顺利执行该语句
    print("BMI: ",user_bmi)
finally: # 不管程序有无异常，均会执行
    print("The End")
