print("How old are you?", end=' ')
age = input()  # 在python3.0之后就没有raw_input()这个函数了
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# study drill 1
# raw_input()（存在于python3.0之前的版本）的作用是接受控制台的用户输入以实现交互。
# 它会将所有输入都看作字符串

# study drill 2
Age = input("How old are you?")
print("You are %s old." % Age)

# study drill 3
print("What's your name?", end=' ')
name = input()
print("Your name is %s." % name)

# study drill 4
# 这里出现反斜线的原因是因为以%r格式化输出的时候，会在对应的输出结果两端加上一对引号，
# 此处针对 6'2" 的两端加上一对单引号，因此为了区别出字符串内部的那个单引号，所以就使用了反斜线
