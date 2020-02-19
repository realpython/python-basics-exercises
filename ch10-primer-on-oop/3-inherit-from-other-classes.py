# 10.3 - Inherit From Other Classes
# Solutions to review exercises


# Exercise 1
# The parent `Dog` class (given in exercise)
class Dog:
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
# Rectangle and Square classes
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


square = Square(4)
print(square.area())
