def mediocre_land():
    print("Maybe your life lacks challenges!")


def heaven():
    print("Congratulations! Welcome to heaven!")


def hell():
    print("Hi! you must do some bad things. Because here is the hell.")


def angel_room():
    print("Hi! I'm an angel, I lose my big diamond. Can you help me find it?")
    print("Please make choice: help or don't")

    choice = input("> ")
    if choice == "help":
        print("You find the diamond, and you have two selections.")
        print("1. You lie to the angel that you don't find. Maybe the diamond will give you a luxurious life.")
        print("2. You give the diamond back to the angel.")

        selection = input("> ")
        if selection == "1":
            print("I'm sorry, you may need more suffering!")
            hell()
        elif selection == "2":
            print("You are a good person.")
            heaven()
        else:
            assert False, "invalid selection"
    elif choice == "don't":
        start()
    else:
        assert False, "invalid choice"


def start():
    print("You are dead. There are two doors.")
    print("If you select the left door, your soul will go to a peaceful but mediocre land.")
    print('''
    If you select the right door, you will encounter a test.
     If you failed the test, your soul will go to the hell.
     If you win, your soul will go to the heaven.
     Of course, after you enter the right room, you will forget what I have said. And you don't know you have died
     ''')
    print("left or right?")

    choice = input("> ")
    if choice == "left":
        mediocre_land()
    elif choice == "right":
        angel_room()
    else:
        assert False, "invalid choice"

start()
