def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")  # Of course I can!

# study drill 2
what_also = age + (height - weight * (iq / 2))
print("The result of the normal formula:", what_also)

# study drill 3
# 题意是让我们修改函数的一部分以产生另一个结果？似乎没什么意义...

# study drill 4
what_new1 = weight - (age + iq / 2 * height)
what_new2 = subtract(weight, add(age, multiply(divide(iq, 2), height)))
print("what_new1:", what_new1)
print("what_new2:", what_new2)
