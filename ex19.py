# 定义一个带有两个形参的函数对象，并分配给函数名cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")  # 打印说明信息
cheese_and_crackers(20, 30)  # 直接传递两个整型数字作为实参


print("OR, we can use variables from our script:")  # 打印说明信息
amount_of_cheese = 10  # 赋值语句
amount_of_crackers = 50  # 赋值语句

cheese_and_crackers(amount_of_cheese, amount_of_crackers)  # 以变量名作为实参来传递数据


print("We can even do math inside too:")  # 打印说明信息
cheese_and_crackers(10 + 20, 5 + 6)  # 可以在实参列表里使用表达式，以表达式返回的对象作为实参


print("And we can combine the two, variables and math:")  # 打印说明信息
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)  # 结合变量和数字来组合成表达式

# study drill 3
def spell(str):
    """
    该函数的功能是将字符串str拼写出来
    :param str:
    :return:
    """
    for char in str:
        print("%r" % char, end=' ')
    print()

str1 = "Hello world!"
str2 = "Hello "
str3 = "world!"
print("直接传递字符串常量")  # 1
spell("Hello world!")

print("传递合并表达式")  # 2
spell("Hello " + "world!")

print("传递变量名")  # 3
spell(str1)

print("传递分片表达式")  # 4
spell(str1[:])

print("变量相加")  # 5
spell(str2 + str3)

print("变量和字符串常量相加")  # 6
spell(str2 + "world!")

print("分片相加")  # 7
spell(str1[:4] + str1[4:])

print("分片和变量相加")  # 8
spell(str1[:6] + str3)

print("分片和字符串常量相加")  # 9
spell(str1[:6] + "world!")

print("索引和字符串常量相加")  # 10
spell(str1[0] + "ello world!")
