# Operators

## 1. Arithmetic Operators

An **arithmetic operation** in Python involves applying mathematical operators to values (operands). Here's the anatomy of an operation:

```python
>>> 10 + 5
15
```

### Arithmetic Operator Symbols and Their Operations

| Operator | Operation           |
| -------- | ------------------- |
| +        | Addition            |
| -        | Subtraction         |
| \*       | Multiplication      |
| /        | Division            |
| //       | Floor Division      |
| %        | Modulus (Remainder) |
| \*\*     | Exponentiation      |

These operators are **binary operators**, meaning they operate on two operands. Let's explore each operator:

```python
>>> 10 + 5   # Addition
15
>>> 10 - 5   # Subtraction
5
>>> 10 * 5   # Multiplication
50
>>> 10 / 5   # Division
2.0
>>> 10 // 5  # Floor Division
2
>>> 10 % 5   # Modulus (Remainder)
0
>>> 10 ** 5  # Exponentiation (Power)
100000
```

### Explanation of Floor Division, Modulus, and Exponentiation

- **`//` Floor Division**: Divides two numbers and returns the integer quotient, discarding any remainder.

  ```python
  >>> 8 // 3
  2  # The quotient is 2, remainder is discarded.
  ```

- **`%` Modulus**: Returns the remainder of a division.

  ```python
  >>> 10 % 3
  1  # The remainder is 1.
  ```

- **`**` Exponentiation\*\*: Raises one number to the power of another.

  ```python
  >>> 2 ** 3
  8  # 2 raised to the power of 3.
  ```

### Division vs Floor Division

The `/` operator performs division and returns the exact result (as a float), while `//` returns only the integer part (quotient).

```python
>>> 5 / 2
2.5  # Standard division
>>> 5 // 2
2    # Floor division
```

### Unary Operators: `+` and `-`

Unlike the binary operators mentioned above, the `+` and `-` operators can also act as **unary operators** (operating on one operand). They indicate positive or negative numbers.

```python
>>> -2    # Unary minus
-2
>>> +2    # Unary plus
2
```

### Variable Usage in Arithmetic Operations

While we've used literals so far, arithmetic operations can also be applied to variables:

```python
>>> x = 1
>>> y = x * 5
>>> print(x, y)
1 5
```

---

## 2. Relational Operators

**Relational operators** are used to compare two values. The result is a boolean (`True` or `False`).

### Relational Operator Symbols and Their Operations

| Operator | Operation                |
| -------- | ------------------------ |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or equal to |
| <=       | Less than or equal to    |
| ==       | Equal to                 |
| !=       | Not equal to             |

These operators are also **binary operators**. Examples:

```python
>>> 10 > 5
True
>>> 10 < 5
False
>>> 10 >= 5
True
>>> 10 <= 5
False
>>> 10 == 5
False
>>> 10 != 5
True
```

Relational operators are also known as **comparison operators**, as they compare two operands and return a boolean value. You can assign the result of a comparison to a variable:

```python
>>> x = 10
>>> y = 15
>>> z = y > x
>>> print(z)
True
```

**Note**: The `==` operator checks for equality and should not be confused with `=` which is used for assignment.

---

## 3. Logical Operators

**Logical operators** are used to combine multiple boolean expressions. They operate on boolean values and return a boolean result.

### Logical Operator Symbols and Their Operations

| Operator | Operation           |
| -------- | ------------------- |
| `not`    | Logical negation    |
| `and`    | Logical conjunction |
| `or`     | Logical disjunction |

- `and` and `or` are **binary operators**.
- `not` is a **unary operator**.

### Examples

```python
>>> True and False
False

>>> True or False
True

>>> x = False
>>> y = not x
>>> print(y)
True
```

The `not` operator inverts the boolean value (`True` becomes `False`, and vice versa). Parentheses can be used but are optional:

```python
>>> x = True
>>> not x
False

>>> x = False
>>> not(x)
True
```

---

## 4. Code Convention

Consider the following lines of code:

```python
>>> print(1 + 2)
3
>>> print(1+2)
3
```

Both lines produce the same output. In this course, we will follow the first convention—**always adding spaces around operators** for readability:

```python
>>> x = 2  # We will follow this.
>>> x=2    # We will NOT follow this.
```

Both are syntactically correct, but adding spaces makes the code more readable.

---

## 5. Expressions

An **expression** in Python is a combination of literals, variables, and operators that evaluates to a value. Here are a few examples:

```python
1 + 4 / 4 ** 0
x / y + z * 2.0
3 > 4 and 1 < 10
not True and False
```

Each expression evaluates to a value, which has a specific type. For example:

- The first two expressions result in a `float`.
- The next two result in a `bool`.

### Arithmetic Expressions

An **arithmetic expression** evaluates to a numeric value (`int` or `float`). Here's an example:

```python
>>> 1 + 2
3
>>> type(1 + 2)
<class 'int'>
```

If one operand is a `float`, the result will also be a `float`:

```python
>>> 1.0 + 2
3.0
>>> type(1.0 + 2)
<class 'float'>
```

### Boolean Expressions

A **boolean expression** results in a `bool` value (`True` or `False`), typically through the use of relational or logical operators:

```python
>>> 2 > 1
True
>>> type(2 > 1)
<class 'bool'>
```

Similarly, logical operators produce boolean results:

```python
>>> True and False
False
>>> type(True and False)
<class 'bool'>
```

#### Truth Tables for Logical Operators

A **truth table** lists all possible outcomes for a logical expression. For example, the truth table for `or` is:

| X     | Y     | X or Y |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

By understanding these operators and how they work in expressions, you'll have a strong foundation to write more complex Python programs.
