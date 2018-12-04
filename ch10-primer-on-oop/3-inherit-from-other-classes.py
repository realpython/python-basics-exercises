# 10.3 - Inherit From Other Classes
# Solutions to review exercises


# Exercise 1
# The parent `Dog` class (given in exercise)
class Dog(object):

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# The GoldenRetriever class that solves the exercise
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


# Exercise 2
# Modified Dog class
class Dog(object):

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        if not isinstance(sound, str):
            raise TypeError("sound should be a string")
        return f"{self.name} says {sound}"
