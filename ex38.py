ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# ten_things.split(' ') which reads as "Call split on ten_things."
#  is split(ten_things, ' ') that means "Call split with arguments ten_things and ' '."
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # more_stuff.pop() which reads as "Call pop on more_stuff."
    #  is pop(more_stuff) that means "Call pop with argument more_stuff."
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # stuff.append(next_one) which reads as "Call append on stuff."
    #  is append(stuff, next_one) that means "Call append with arguments stuff and next_one."
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
# stuff.pop() which reads as "Call pop on stuff."
#  is pop(stuff) that means "Call pop with argument stuff."
print(stuff.pop())
# ' '.join(stuff) which reads as "Call join on ' '."
#  is join(' ', stuff) that means "Call join with arguments ' ' and stuff."
print(' '.join(stuff))  # what? cool!
# '#'.join(stuff[3:5]) which reads as "Call join on '#'."
#  is join('#', stuff[3:5]) that means "Call join with arguments '#' and stuff[3:5]."
print('#'.join(stuff[3:5]))  # super stellar!
