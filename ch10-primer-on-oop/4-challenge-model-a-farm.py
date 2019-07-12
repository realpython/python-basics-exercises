# 10.4 - Challenge: Model a Farm
# Solutions to challenge


class Animal:

    # Class attributes
    stuff_in_belly = 0
    position = 0

    # Initializer
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Instance methods
    def talk(self, sound=None):
        """Return the string "<name> says <sound>"

        If `sound` is left out, returns "Hello, I'm <name>"
        """
        if sound is None:
            return f"Hello. I'm {self.name}!"
        return f"{self.name} says {sound}"

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
    def talk(self, sound="Bark Bark!"):
        return super().talk(sound)

    def fetch(self):
        return f"{self.name} is fetching."


class Sheep(Animal):
    def talk(self, sound="Baaa Baaa"):
        return super().talk(sound)


class Pig(Animal):
    def talk(self, sound="Oink Oink"):
        return super().talk(sound)


# The following code illustrates how to use the classes defined above.
# It is not necesarrily a part of the solution, and is included for
# illustration purposes only.

# Create a dog
dog = Dog("Blitzer", "yellow")

# Output the dog's attributes
print(f"Our dog's name is {dog.name}.")
print(f"And he's {dog.color}.")

# Output some behavior
print(f"Say something, {dog.name}.")
print(dog.talk())
print("Go fetch!")
print(dog.fetch())

# Walk the dog
print(f"{dog.name} is at position {dog.walk(2)}.")

# Run the dog
print(f"{dog.name} is now at position {dog.run(4)}")

# Feed the dog
print(dog.feed())

# Is the dog hungry?
print(dog.is_hungry())

# Feed the dog more
print(dog.feed())
print(dog.feed())
print(dog.is_hungry())
print(dog.feed())

print("\n")

# Create a sheep
sheep = Sheep("Shaun", "white")

# The sheep talks!
print(sheep.talk())

# When the sheep runs, the distance is returned
print(sheep.run(2))
print(sheep.run(2))

print("\n")

# Create a pig
pig = Pig("Carl", "pink")

# Pigs love to oink!
print(pig.talk())
