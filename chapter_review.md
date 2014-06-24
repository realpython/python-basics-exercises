# Chapter Questions

## Getting Started

1. What’s the difference between a variable and a value?
    - A variable is a name for a value while a value is an integer, string, list, etc.

## Interlude: Leave yourself helpful notes

1. What does it mean to comment your code?
    - Comments are used to add helpful notes in order to document what's happening.

1. Show examples of single and multiple line comments.

    ```python
    # single line
    def add_one(num):
        # Returns num plus one
        return num + 1

    # multi line
    def add_one(num):
        """
        This function takes an integer or float as it's
        argument and returns that number plus one.
        """
        return num + 1
    ```

## Strings and Methods

1. What does it mean to concatenate a string?
    - String concatenation is used to join two strings together, using the `+` operator.

1. What will `"REAL PYTHON".lower()` return?
    - `'real python'`

## Fundamentals: Working with Strings

1. What’s the difference between an integer and a floating-point?
    - Integers store whole numbers (i.e., 1, 2, 200, 9876, etc.) while a floating-point (or float) store numbers with decimals (i.e., 2.456, 9.0, 100.7, etc.).

1. Assuming Python 2.x, what will be printed - `print 'My first name is not {1}.'.format("John", "Doe")`?
    - Output: `My first name is not  Doe.`

1. Assuming Python 2.x, what will be printed - `print 'My last name is not {first_name}.'.format(first_name="John", last_name="Doe")`?
    - Output: `My last name is not John.`

## Fundamentals: Functions and Loops

1. What's the purpose of indentation in Python code?
    - Code blocks - like functions, if statements, loops, etc. - are defined by indentation. Indenting starts a block, while unindenting ends it. In other words, indentation is how the Python interpreter knows that code is inside of a block. As soon as the interpeter sees a line that isn't indented, that's the end of the block.

1. Assuming Python 2.x, what will be printed - `print type(9/10)`?
    - In Python 2.x, dividing two integers yields an integer; the remainder is dropped.

1. What will be printed in the following situation?

    ```
    def placeholder():
        pass

    print type(placeholder())
    ```

    The output will be `<type 'NoneType'>`. Why is that?

1. Assuming Python 3.x, what will be printed - `print(type(9/10))`?
    - In Python 3.x, dividing two integers yields a float.

1. What will this, `print 5.5 // 2`, snippet yield?
    - This will yield `2.0` since the `//` operator is used for flooring division.

## Fundamentals: Conditional logic

1. What are boolean values?
    - A boolean can only take on one of two values: True or False.

1. What’s the difference between `=` and `==`?
    - `=` is used for assignment; so, assigning values from the right side of the operand to the left. `==` checks to see if the values on either side of the operad are True or False.

1. What will be printed in the following situation? Why?

    ```
    x = True
    y = False
    z = False

    print x OR y And z
    ```

    Answer: `True` will be printed because `AND` has a higher precedence than `OR` - so it's evaluated first.


## Fundamentals: Lists and Dictionaries

1. Assuming Python 2.x, what will be printed - `print type([9/10])`?
    - This yields will yield `<type 'list'>`.

1. Given the list, `my_list = [6, "four", 5]`, how would you reassign the second element to the integer 4?
    - `my_list[1] = 4`

1. What's the difference between the `sorted()` function and the `.sort()` method?
    - `sorted()` is a builtin that makes a copy of the list you wish to sort, then returns a new sorted list. `.sort()`, meanwhile, sorts the list in place; it does not make a copy. `sorted()` can be used on any iterable not just lists, while `.sort()` is just for lists.


## File Input and Output

1. What's an escape character?
    - An escape character is used along another character to represent a different, usually more complex, character. Together, this is called an escape sequence. For example, the escape sequence `\n` (where '\' is the escape character and `n` is the additional character) is interpreted by Python as a newline character while `\t` represents a tab character. Check out the official Python [documentation](https://docs.python.org/2/reference/lexical_analysis.html#string-literals) to view more examples of escape sequences.
