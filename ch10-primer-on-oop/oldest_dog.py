class Dog():

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object
jake = Dog("Jake", 7)
doug = Dog("Doug", 4)
william = Dog("William", 5)


# Determine the oldest dog
def get_biggest_number(*args):
    return max(args)

# output
print("The oldest dog is {} years old.".format(
    get_biggest_number(jake.age, doug.age, william.age)))
