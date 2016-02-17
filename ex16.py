from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input('?')

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')
target.write("%s\n%s\n%s\n" % (line1, line2, line3))  # study drill 3

print("And finally, we close it.")
target.close()

# study drill 4, 5
# 参数'w'表示以可写的模式打开文件，
# 如果文件中有内容会自动先清除，不需要额外调用truncate方法
