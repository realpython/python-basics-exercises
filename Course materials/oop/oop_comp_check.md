## Questions

1. What's a class?
2. What's an instance?
3. What's the relationship between a class and an instance?
4. What's the Python syntax used for defining a new class?
5. What's the spelling convention for a class name?
6. How do you instantiate, or create an instance of, a class?
7. How do you access the attributes and behaviors of a class instance?
8. What's a method?
9. What's the purpose of `self`?
10. What's the purpose of the `__init__` method?
11. Describe how inheritence helps prevent code duplication.
12. Can child classes override properties of their parents?

## Answers

1. A class is a mechanism used to create new user-defined data structures. It contains data as well as the methods used to process that data.
2. An instance is a copy of the class with *actual* values, literally an object of a specific class. 
3. While a class is a blueprint used to describe how to make something, instances are objects created from those blueprints.
4. `class PythonClassName():`
5. CamelCase notation, starting with a capital letter - i.e., `PythonClassName()`
6. You use the the class name, followed by parentheses. So if the class name is `Dog()`, an dog instance would be - `my_class = Dog()`.
7. With dot notation - e.g., `instance_name.attribute_name`
8. A function that's defined inside a class.
9. The first argument of every method references the current instance of the class, which by convention, is named `self`. In the `__init__` method, `self` refers to the newly created object; while in other methods, `self` refers to the instance whose method was called. For more on `__init__` vs. `self`, check out [this](http://stackoverflow.com/a/625098) article.
10. The `__init__` method initializes an instance of a class. 
11. Child classes inheriet all of the parent's attributes and behaviors. 
12.
 