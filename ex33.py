# study drill 1, 2, 3, 4
def append_nums_w(l, top, increment=1):
    i = 0
    while i < top:
        print("At the top i is %d" % i)
        l.append(i)
        i += increment
        print("Numbers in l now: ", l)
        print("At the bottom i is %d" % i)


# study drill 5
def append_nums_f(l, top, increment=1):
    for i in range(0, top, increment):
        l.append(i)
        print("Numbers in l now: ", l)

numbers = []
append_nums_w(numbers, 6, 3)

print("The numbers: ")
for num in numbers:
    print(num)
