# Parent class
class Dog():

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return self.name, self.age

    # instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)


# child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# child classes have specific attributes
# and behaviors as well
print(jim.run("slow"))

# is jim an instance of Dog()?
print(isinstance(jim, Dog))

# is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# is johnny walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# is julie and instance of jim?
print(isinstance(julie, jim))
