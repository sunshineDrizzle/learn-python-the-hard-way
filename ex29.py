people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

# study drill 1
# if语句对其内部的代码做了一个选择性的执行，即只在条件为真时执行。
# 是一种选择或是判断

# study drill 2
# 缩进是为了分清楚代码属于哪一层次，同一层次的代码需要有相同的缩进
# 至于这里缩进4个空格是因为PEP8编码风格要求缩进是4的倍数的空格

# study drill 3
# 如果不缩进的话，程序会认为这些代码不是if语句内的，而是和if属于同一个层次

# study drill 4
if dogs != cats:
    print("Dogs are not cats")
