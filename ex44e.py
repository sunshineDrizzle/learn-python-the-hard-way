class Other:

    def implicit(self):
        print("OTHER implicit()")

    def override(self):
        print("OTHER override()")

    def altered(self):
        print("OTHER altered()")


class Child:

    def __init__(self):
        self.other = Other()  # 就是把另一个类的实例作为Child类的一部分来获得它的一些属性

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

# study drill
# 本次的study drill就是建议我们使用PEP8的编码风格，关于这个我发现pycharm这个IDE自带依据PEP8来纠正程序员的编码风格的机制，
# 因此，用这个IDE可以在平时的使用中慢慢纠正和熟悉PEP8的编码风格
