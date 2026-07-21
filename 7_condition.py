"""
if condition: //条件
    print("condition is true") //执行
else:
    print("condition is false")
"""
user_height=input("Enter your height in meters: ")
user_weight=input("Enter your weight in kg: ")
user_bmi=float(user_weight)/(float(user_height)**2)
if user_bmi>18.5 and user_bmi<=23.9 : # if 18.5<user_bmi<=23.9
    print("Your BMI value is normal: ",user_bmi)
else:
    if user_bmi<=18.5:
        print("Your BMI is low: ",user_bmi)
    else:
        print("Your BMI is high: ",user_bmi)

"""
多条件
if condition1:
    执行语句
elif condition2:
    执行语句
else:
    执行语句
"""

"""
逻辑词：and or not
"""