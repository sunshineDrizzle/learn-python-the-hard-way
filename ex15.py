from sys import argv  # 从sys模块中导入属性argv

script, filename = argv  # 将从命令行传入的两个实参赋值给两个变量

txt = open(filename)  # 打开名为filename的文件，将文件对象赋值给变量txt

print("Here's your file %r:" % filename)  # 打印一条说明信息
print(txt.read())  # 调用文件对象的read方法，打印文件内容

print("Type the filename again:")  # 打印一条提示信息
file_again = input("> ")  # 打印一个输入提示符，提示输入文件名

txt_again = open(file_again)  # 打开文件，并将返回的文件对象赋值给变量txt_again

print(txt_again.read())  # 调用文件对象的read方法，打印文件内容
