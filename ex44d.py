class Parent:

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()  # 第三种情况的重点在这里，利用super调用超类中的方法，如果有多个超类（注意方法解析次序MRO），super会自行找出合适的目标
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# override和alter的区别：
# 顾名思义，override是覆盖，重写，意思是子类中的方法完全替代了超类中的同名方法
# 而alter是更改的意思，也就是说通过在子类方法的重写过程中运行超类的同名方法，就相当于子类方法中包含着超类中的方法内容
# 因此是保留了超类中的方法内容，而在此基础上做些改变
