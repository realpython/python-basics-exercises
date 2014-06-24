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

## Fundamentals: Functions and Loops

1. What's the purpose of indentation in Python code?
    - Code blocks - like functions, if statements, loops, etc. - are defined by indentation. Indenting starts a block, while unindenting ends it. In other words, indentation is how the Python interpreter knows that code is inside of a block. As soon as the interpeter sees a line that isn't indented, that's the end of the block.

1. Assuming Python 2.7.x, what will be printed - `print type(9/10)`?
    - In Python 2.7.x, dividing two integers yields an integer; the remainder is dropped.

## Fundamentals: Conditional logic

1. What are boolean values?
    - A boolean can only take on one of two values: `True` or `False`.

# File Input and Output

1. What's an escape character?
    - An escape character is used along another character to represent a different, usually more complex, character. Together, this is called an escape sequence. For example, the escape sequence `\n` (where '\' is the escape character and `n` is the additional character) is interpreted by Python as a newline character while `\t` represents a tab character. Check out the official Python [documentation](https://docs.python.org/2/reference/lexical_analysis.html#string-literals) to view more examples of escape sequences.
