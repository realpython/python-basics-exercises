# 10.4 - Assignment: Model a Farm
# Solutions to assignment


class Animal:

    # Class attributes
    stuff_in_belly = 0
    position = 0

    # Initializer
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Instance methods
    def talk(self):
        return f"Hello. I'm {self.name}"

    def walk(self, walk_increment):
        self.position = self.position + walk_increment
        return self.position

    def run(self, run_increment):
        self.position = self.position + run_increment
        return self.position

    def feed(self):
        self.stuff_in_belly = self.stuff_in_belly + 1
        if self.stuff_in_belly > 3:
            return self.poop()
        else:
            return f"{self.name} is eating."

    def is_hungry(self):
        if self.stuff_in_belly < 2:
            return f"{self.name} is hungry"
        else:
            return f"{self.name} is not hungry"

    def poop(self):
        self.stuff_in_belly = 0
        return "Ate too much ... need to find a bathroom"


class Dog(Animal):

    def talk(self):
        return "Bark! Bark!"

    def fetch(self):
        return f"{self.name} is fetching."


class Sheep(Animal):

    def talk(self):
        return "Baaa Baaa"


class Pig(Animal):

    def talk(self):
        return "Oink Oink"


# create a dog
dog = Dog("Blitzer", "yellow")
# output the dog's attributes
print(f"Our dog's name is {dog.name}.")
print(f"And he's {dog.color}.")
# output some behavior
print(f"Say something, {dog.name}.")
print(dog.talk())
print("Go fetch!")
print(dog.fetch())
# walk the dog
print(f"{dog.name} is at position {dog.walk(2)}.")
# run the dog
print(f"{dog.name} is now at position {dog.run(4)}")
# feed the dog
print(dog.feed())
# is the dog hungry
print(dog.is_hungry())
# feed the dog more
print(dog.feed())
print(dog.feed())
print(dog.is_hungry())
print(dog.feed())

print("\n")

sheep = Sheep("Shaun", "white")
print(sheep.talk())
print(sheep.run(2))
print(sheep.run(2))

print("\n")

pig = Pig("Carl", "pink")
print(pig.talk())
