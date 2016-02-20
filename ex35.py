from sys import exit


def gold_room():
    print("This room is full of gold.  How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        try:
            how_much = float(choice)  # 允许浮点输入
        except ValueError:  # 捕捉用户不规范的输入，并给出处理
            dead("Man, learn to type a number.")

        if how_much < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            dead("You greedy bastard!")
    else:
        dead("Man, learn to type a number.")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "fight with bear":  # study drill 4
            dead("You are a brave man. However, you are dead.")
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

# study drill 5
# 题目中的bugs应该是指用户输入带小数点（原题用的是int()，我改成了float()）且包含1或0的数字字符串会引发错误（事实上输入非数字的字符也会出错）
# int()函数的作用如下：
# 如果没有参数则返回0
# 如果参数只有一个且是数字，则返回一个去掉小数部分（如果有的话）的整数对象
# 如果参数只有一个且是字符串，则该字符串必须是用来表示整数的，此时会传入一个默认的参数base=10，返回与字符串所表示数字值相同的整型对象
# 如果参数有两个，则base参数是用来指出另一个参数的进制的。
