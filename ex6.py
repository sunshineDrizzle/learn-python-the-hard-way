x = "There are %d types of people." % 10  # 使用十进制整数形式的格式化字符将整数10嵌入字符串
binary = "binary"  # 将字符串赋值给变量名
do_not = "don't"  # 将字符串赋值给变量名
y = "Those who know %s and those who %s." % (binary, do_not)  # 使用字符串形式的格式化字符将字符串嵌入字符串

print(x)  # 打印操作
print(y)  # 打印操作

print("I said: %r." % x)  # 使用字符串形式（repr）的格式化字符将字符串嵌入字符串
print("I also said: '%s'." % y)  # 使用字符串形式的格式化字符将字符串嵌入字符串

hilarious = False  # 将布尔值赋值给变量名
joke_evaluation = "Isn't that joke so funny?! %r"  # 将包含格式化字符的字符串赋值给变量名

print(joke_evaluation % hilarious)  # 打印字符串格式化表达式返回的结果

w = "This is the left side of..."  # 将字符串赋值给变量名
e = "a string with a right side."  # 将字符串赋值给变量名

print(w + e)  # 合并两个字符串，此处的加号是经过操作符重载的，所以可以用于合并两个字符串
