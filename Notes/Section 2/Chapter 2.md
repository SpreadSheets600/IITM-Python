# Input

## Accepting Input from the User

Accepting input from the user is a common operation in programming. Any piece of software needs a functional interface to interact with the user. For example, on apps like Facebook, Instagram, and Twitter, the text entered in comment boxes is considered input. This input is processed by code in the backend and displayed as a comment.

Python provides a built-in function `input()` to accept input from the user. It’s simple yet powerful:

```python
x = input()
print('The input entered by the user is', x)
```

In this case, the interpreter waits for you to enter text. Once you press enter, the input is stored in the variable `x`. The output looks like this:

```python
1
The input entered by the user is 1
```

You can also prompt the user to enter a specific type of input by passing a string argument to the `input()` function:

```python
x = input('Enter an integer between 0 and 10: ')
print('The number entered by the user is', x)
```

Now, let’s examine the type of the variable `x`:

```python
x = input()
print('The input entered by the user is of type', type(x))
```

No matter what you enter (integer, float, string, or boolean), the `input()` function always returns a string. If the user enters `123`, it's processed as the string `'123'`.

---

## Type Conversion

If you want to convert a string into an integer, Python provides the built-in function `int()`:

```python
x = '123'
print('The type of x is', type(x))
y = int(x)
print('The type of y is', type(y))
```

This process is called type conversion. You can also convert an integer to a string using the `str()` function:

```python
x = 123
print('The type of x is', type(x))
y = str(x)
print('The type of y is', type(y))
```

To accept an integer input from the user, you can convert the string returned by `input()` into an integer:

```python
x = int(input('Enter an integer: '))
print('The integer entered by the user is', x)
```

You can also combine the two operations in one line:

```python
x = int(input())
print('The integer entered by the user is', x)
```

In this case, the output of the `input()` function is passed as an argument to `int()`. Be careful, though! If the user enters a float value, the following code will raise a `ValueError`:

```python
x = int(input())    # user enters a float value here
```

---

## Built-in Functions

We’ve been using the term _built-in functions_ often. These are predefined functions in Python that accept inputs and produce outputs. For example, `print()` is a built-in function that accepts input and prints it to the console. Here are a few more useful built-in functions:

- **`round()`**: Accepts a number and returns the closest integer. Example: `round(1.2)` returns `1`, while `round(1.9)` returns `2`.
- **`abs()`**: Accepts a number and returns its absolute value. Example: `abs(-1.2)` returns `1.2`.
- **`int()`**: Converts a string representing an integer into an `int`. Example: `int('123')` returns `123`. If a float is passed, the decimal part is discarded. Example: `int(1.2)` returns `1`, and `int(-2.5)` returns `-2`.
- **`pow()`**: Accepts two arguments and returns the value of `x ** y`. Example: `pow(2, 3)` returns `8`. It also supports a third argument: `pow(x, y, z)` returns `(x ** y) % z`.
- **`isinstance()`**: Used to check if an object is of a specific type. Example: `isinstance(3, int)` returns `True`, and `isinstance('hello', str)` also returns `True`.

The Python documentation provides a complete list of built-in functions for more reference.
