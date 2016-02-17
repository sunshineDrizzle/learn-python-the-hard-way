from sys import argv  # 从模块sys中导入属性argv

script, input_file = argv  # 解包赋值


def print_all(f):  # 定义函数
    print(f.read())


def rewind(f):  # 定义函数
    f.seek(0)  # 将当前位置移到索引为0的地方


def print_a_line(line_count, f):  # 定义函数
    print(line_count, f.readline())

current_file = open(input_file)  # 打开文件，将返回的文件对象赋值给变量名

print("First let's print the whole file:\n")
print_all(current_file)  # 函数调用

print("Now let's rewind, kind of like a tape.")
rewind(current_file)  # 函数调用

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)  # 函数调用

current_line += 1
print_a_line(current_line, current_file)  # 函数调用

current_line += 1
print_a_line(current_line, current_file)  # 函数调用

# study drill 2
# 变量current_line中对应的是当前输出行的行号，
# 通过每调用一次print_a_line函数就加1的方法来计数

# study drill 4
# 文件对象的seek方法的功能是设置文件的当前位置的偏移
