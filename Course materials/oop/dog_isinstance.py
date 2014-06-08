# Parent class
class Dog(object):

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


# sub-class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# sub-class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# sub-classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print jim.description()

# sub-classes have specific attributes
# and behaviors as well
print jim.run("slow")

# is jim an instance of Dog()?
print isinstance(jim, Dog)

# is julie an instance of Dog()?
julie = Dog("Julie", 100)
print isinstance(julie, Dog)

# is julie and instance of jim?
print isinstance(julie, jim)