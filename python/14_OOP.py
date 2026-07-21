# 创建类
class Student:
    def __init__(self, name, id, chinese, math, english): #构造函数必须用 __init__(self,……)
        self.name = name
        self.id = id
        self.chinese=chinese
        self.math=math
        self.english=english
    # 计算语数英总成绩
    def sum_score(self):
        return self.math+self.english+self.chinese
    # 打印学生信息
    def print_info(self):
        print("Name:{:<6}ID:{:<10}TotalScore:{:<5}".format(self.name,self.id,self.sum_score()))
# 实例化对象
stu1 = Student("Amy","25143768",112,134,136)
stu2 = Student("Bob","25149203",102,126,140)
stu1.print_info()
stu2.print_info()

# 利用字典存储不同科目的成绩
"""
class Student:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.grades={"math":0,"science":0,"english":0}
    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade     
"""

# 继承
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        print(self.name," is speaking")

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def speak(self):
        print(self.name," Wolf!Wolf!")
class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def speak(self):
        print(self.name," Meow!Meow!")

dog = Dog("Dog",2)
cat = Cat("Cat",3)
dog.speak()
cat.speak()

"""
1.如何写子类构造函数？ 利用 super().__init__(……)
2.当子类和父类中的函数重名时，会调用谁的函数？ 子类
"""

