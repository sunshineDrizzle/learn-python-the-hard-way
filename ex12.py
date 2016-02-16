age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# study drill 1
# 由于我使用的python3.5中没有raw_input，
# 所以我在命令行中输入的是python -m pydoc input以代替前者
# 查出的文档中说明input的功能是从标准输入中读取字符串，也可以在读取输入之前输出提示信息

# study drill 3
# pydoc的作用和help类似，都可以调出各模块和函数的文档字符串（docstring）
# 不过pydoc可以将docstring转成HTML输出
