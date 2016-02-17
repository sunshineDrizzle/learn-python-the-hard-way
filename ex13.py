from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# study drill 1，2
# 错误提示我们程序需要在命令行传递四个实参解包给四个变量，不能多也不能少。

# study drill 3
name = input("What's your name?")
print("Your name is:", name)
