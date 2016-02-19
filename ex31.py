print("You enter a dark room with two doors.  Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.  What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Go out of the door at first.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    elif bear == "3":
        print("OK, you give up the game!")
    else:
        print("Well, doing %s is probably better.  Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.  Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.  Good job!")

else:
    print("You stumble around and fall on a knife and die.  Good job!")

# study drill 2
print("Now, you can get one of the two skills:\n1. fly\n2. dive\nWhich one you'd like to choose?")
skill = input("> ")

if skill == "1":
    print("You fly to the sky and meet a eagle.")
    print("1. You greet the eagle ruggedly.")
    print("2. You greet the eagle cravenly.")
    greet = input("> ")

    if greet == "1":
        print("The eagle is scared and runs away. Good job!")
    elif greet == "2":
        print("The eagle attack you. Then, you drop down!")
    else:
        print("Nothing happens.")

elif skill == "2":
    print("You dive at an ocean and meet a shark.")
    print("1. You greet the shark ruggedly.")
    print("2. You greet the shark cravenly.")
    greet = input("> ")

    if greet == "1":
        print("The shark is angry and eats you!")
    elif greet == "2":
        print("The shark is complacent and go away.")
    else:
        print("The shark is angry because of your neglect and eats you!")

else:
    print("A lion eats you because you can't fly or dive!")
