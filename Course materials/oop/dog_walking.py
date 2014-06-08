# parent class
class Pet(object):

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print dog.walk()


# parent class
class Dog(object):

    # class attribute
    species = 'mammal'

    # initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return self.name, self.age

    # instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    def walk(self):
        return "%s is walking!" % (self.name)


# sub-class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# sub-class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

# create instances of dogs
my_dogs = [Bulldog("Tom", 6), RussellTerrier("Fletcher", 7), Dog("Larry", 9)]

# instantiate the Pet() class
my_pets = Pet(my_dogs)

# output
my_pets.walk()
