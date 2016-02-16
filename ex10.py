tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''  # 偏爱用'''而不是"""的原因大概是前者比较方便从键盘键入吧？，我是这么认为的

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# study drill 3
print("line1%sline2" % '\n')

# study drill 4
print("%r是单引号\n%r是双引号" % ('\'', '\"'))
print("%s是单引号\n%s是双引号" % ('\'', '\"'))
# 发现以%r格式输出时会自动带上一对引号，而%s则不会。我觉得没有优劣之分，各自有不同的用处罢了。
