the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
'''
for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)
'''
# study drill 2 -> assigned range(0,6) directly to elements
elements.extend(range(0, 6))

# now we can print them out too
for i in elements:
    print("Element was: %d" % i)

# study drill 1
# range(0, 6)会返回一个以1为步进的0~5的整数迭代器

# study drill 3
# 列表自带的方法还有clear（清除列表中的所有元素）；extend（为列表添加来自迭代器的元素）
# insert（在指定位置插入元素）；reverse（翻转元素顺序）
