# 读文件
f=open("./5_Interaction_mode.txt","r",encoding="utf-8") #在同一文件夹下可直接传入相对路径
print(f.read()) # 会读全部的文件内容，并打印
print(f.read()) # 会读空字符串，并打印（第一次读文件已经读到了文件末尾）
"""
1.
在读很大内存的文件时，可以给read传入数字
print(f.read(10)) # 会读第1-10个字节的文件内容
print(f.read(10)) # 会读第11-20个字节的文件内容
2.
print(f.readline()) #会读一行文件内容，如果读到文件末尾会返回空字符串
3.
lines = f.readlines() # 把每行内容储存到列表里
for line in lines: # 遍历每行内容
    print(line) # 打印当前行
"""
f.close() # 关闭文件，释放资源
"""用以下方法可以避免“由于忘记close而导致资源泄漏”的问题
#with open("./5_Interaction_mode.txt","r",encoding="utf-8") as f:
    print(f.read()) 
"""
# 写文件
with open("./test.txt","w",encoding="utf-8") as f: # 只写模式
    f.write("Hello!\n")
    f.write("World!\n") # write不具备自动换行功能，需要手动换行
with open("./test.txt","a",encoding="utf-8") as f: # 追加模式
    f.write("Hello!\n")
    f.write("World!\n")
with open("./test.txt","r+",encoding="utf-8") as f: # 读写模式，write调用后会以追加的模式进行
    f.write("Hello!\n")
    f.write("World!\n")
    print(f.read())