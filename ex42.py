# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    # study drill 3
    def eat(self):
        print("Oh, that's delicious!")


# Dog is-a Animal
# Dog has-a __init__ that takes self and name parameters
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a attribute named name
        self.name = name


# Cat is-a Animal
# Cat has-a __init__ that takes self and name parameters
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a attribute named name
        self.name = name


# Person is-a object
# Person has-a __init__ that takes self and name parameters
class Person(object):

    def __init__(self, name):
        # Person has-a attribute named name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

    # study drill 3
    def speak(self):
        print("Can you speak Chinese?")


# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # 找到Employee的超类也就是Person，再调用Person的__init__
        super(Employee, self).__init__(name)
        # Employee has-a attribute named salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    # study drill 3
    def swim(self):
        print("I'm swimming!")


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a instance of class Dog
rover = Dog("Rover")

# satan is-a instance of class Cat
satan = Cat("Satan")

# mary is-a instance of class Person
mary = Person("Mary")

# mary has-a attribute named pet. Now set it as satan.
mary.pet = satan

# frank is-a instance of class Employee
frank = Employee("Frank", 120000)

# frank has-a attribute named pet. Now set it as rover
frank.pet = rover

# flipper is-a instance of class Fish
flipper = Fish()

# crouse is-a instance of class Salmon
crouse = Salmon()

# harry is-a instance of class Halibut
harry = Halibut()

# study drill 1
# 在python3.0以前，要声明一个类为新式类的话必须要继承自object基类

# study drill 2
# 通过重载的方法可以使得类的使用类似于基本的核心类型

# study drill 3
rover.eat()
mary.speak()
flipper.swim()
