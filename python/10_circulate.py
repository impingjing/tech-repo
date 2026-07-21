"""
while conditionA:
    actionB
"""
list1=["I","am","a","te","n","a","t"]
#以下三种方法结果一样
for i in list1:
    print(i)

for i in range(len(list1)):
    print(list1[i])

i=0
while i<len(list1):
    print(list1[i])
    i=i+1

num=input("Enter a number (q to quit):")
total=0
count=0
while num!="q":
    total=total+int(num)
    count=count+1
    num=input("Enter a number (q to quit):")
print("Average:",total/count)