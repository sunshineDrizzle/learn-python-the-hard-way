name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

# study drill 2:
height_cm = height * 2.54
weight_kg = weight * 0.45359
print("He's %f centimeters tall." % height_cm)
print("He's %f kilograms heavy." % weight_kg)

# study drill 4:
print("15的十六进制是%x" % 15)
print("以浮点指数形式输出3141: %e" % 3141)

'''
study drills：
对于study drill 1，只要用替换工具，在被替换栏输入my_, 替换栏不输入任何东西即可
'''