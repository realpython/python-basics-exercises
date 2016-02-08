class Animal(object):

    # class attributes
    stuff_in_belly = 0
    position = 0

    # initializer
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # instance methods
    def talk(self):
        return "Hello. I'm {}".format(self.name)

    def walk(self, walk_increment):
        self.position += walk_increment
        return self.position

    def run(self, run_increment):
        self.position += run_increment
        return self.position

    def feed(self):
        self.stuff_in_belly += 1
        if self.stuff_in_belly > 3:
            return self.poop()
        else:
            return "{} is eating.".format(self.name)

    def hungry(self):
        if self.stuff_in_belly < 2:
            return "{} is hungry".format(self.name)
        else:
            return "{} is not hungry".format(self.name)

    def poop(self):
        self.stuff_in_belly == 0
        return "Ate too much ... need to find a bathroom"


class Dog(Animal):

    def talk(self):
        return "Bark! Bark!"

    def fetch(self):
        return "{} is fetching.".format(self.name)


class Sheep(Animal):

    def talk(self):
        return "Baaa Baaa"


class Pig(Animal):

    def talk(self):
        return "Oink Oink"


# create a dog
dog = Dog("Blitzer", "yellow")
# output the dog's attributes
print "Our dog's name is {}.".format(dog.name)
print "And he's {}.".format(dog.color)
# output some behavior
print "Say something, {}.".format(dog.name)
print dog.talk()
print "Go fetch!"
print dog.fetch()
# walk the dog
print "{} is at position {}.".format(dog.name, dog.walk(2))
# run the dog
print "{} is now at position {}".format(dog.name, dog.run(4))
# feed the dog
print dog.feed()
# is the dog hungry
print dog.hungry()
# feed the dog more
print dog.feed()
print dog.feed()
print dog.hungry()
print dog.feed()

print "\n"

sheep = Sheep("Shaun", "white")
print sheep.talk()
print sheep.run(2)
print sheep.run(2)

print "\n"

pig = Pig("Carl", "pink")
print pig.talk()
