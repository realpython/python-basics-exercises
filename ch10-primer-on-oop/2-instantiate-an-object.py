# 10.2 - Instantiate an Object
# Solutions to review exercises


# Exercise 1
class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# The value for `age` can vary in your solution
philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")


# Exercise 2
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,} miles")


# Exercise 3
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, miles):
        self.mileage = self.mileage + miles


blue_car = Car("blue", 0)
blue_car.drive(100)
print(blue_car.mileage)
