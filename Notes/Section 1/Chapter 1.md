# Literals and Variables

In Python, **literals** represent fixed values like `'Hello, World!'` or numbers such as `1` and `2.0`. A literal is a direct representation of a constant value in your code. **Variables**, on the other hand, are used to store these values. You can think of variables as labeled containers that hold data, allowing you to reference and manipulate that data later.

## Defining Variables

In Python, variables are defined using the assignment operator `=`. Here’s how you can assign values to variables:

```python
>>> x = 1
>>> print(x)
1

>>> y = 'a string'
>>> print(y)
a string

>>> foo_bar = 123.456
>>> print(foo_bar)
123.456
```

## The Assignment Operator `=`

The `=` operator is used for two main purposes:

1. **Defining a new variable**
2. **Updating an existing variable**

For example:

```python
>>> x = 1       # Define a new variable
>>> x = x + 1   # Update the existing variable by adding 1 to its value
>>> print(x)
2
```

## Right-to-Left Evaluation

The assignment operator evaluates expressions from right to left. This means the expression on the right of `=` is evaluated first, and the result is assigned to the variable on the left.

---

## Basic Data Types and the `type()` Function

Python offers several **basic data types** to represent different kinds of data. Some of the most common types include:

- **Integer (`int`)**
- **Float (`float`)**
- **String (`str`)**
- **Boolean (`bool`)**

You can use the `type()` function to check the type of any object in Python.

### Integer (`int`)

Integers are whole numbers, either positive or negative. Here’s an example:

```python
>>> print(1)
1

>>> type(1)
<class 'int'>
```

### Float (`float`)

Floats are numbers that contain decimal points, representing real numbers. Both `1.0` and `1.` are valid float literals in Python:

```python
>>> print(1.0)
1.0

>>> type(1.0)
<class 'float'>

>>> print(1.)
1.0
```

In Python, `1.` and `1.0` are equivalent and represent the same float value.

### String (`str`)

Strings are sequences of characters, enclosed within single quotes `' '` or double quotes `" "`:

```python
>>> print('one')
one

>>> type("one")
<class 'str'>
```

### Boolean (`bool`)

Booleans represent truth values and can only have two possible outcomes: `True` or `False`. Note that in Python, these values are case-sensitive. Lowercase `true` and `false` are not recognized as valid boolean values.

```python
>>> print(True)
True

>>> type(False)
<class 'bool'>
```

---

## Comments in Python

**Comments** are lines of code that the Python interpreter ignores. Comments help make your code easier to understand, but they don’t affect how the program runs. In Python, a comment starts with the `#` symbol.

### Single-Line Comments

```python
>>> # This is a comment
>>> # print(1)
```

Since the second line is a comment, the statement `print(1)` is not executed, and no output is produced.

### Inline Comments

You can also add comments at the end of a line of code:

```python
>>> print(1)  # This line prints the number 1
1
```
