import ex40_mystuff


class MyStuff:
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I'm classy apples!")

# dict style
mystuff = {"apple": "I AM APPLES!"}
print(mystuff["apple"])

# module style
ex40_mystuff.apple()
print(ex40_mystuff.tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)
