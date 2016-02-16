print("How old are you?", end=' ')
age = input()  # 在python3.0之后就没有raw_input()这个函数了
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))
