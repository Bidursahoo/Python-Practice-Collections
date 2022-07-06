class mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking  ")

    def cute(self):
        print(f"{self.name} is cute")


class dog(mammal):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Barking")


class cat(mammal):
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("MEow")


bar = dog(dog)
bar.cute()
