# Arithmetic Expressions: Precedence and Order

## Precedence of Operators

When an expression has multiple operators, Python follows a predefined order of precedence to determine how to evaluate it. For example:

```python
>>> 4 // 2 - 1
1
```

In this case, the `//` operator (floor division) has higher precedence than `-` (subtraction), so it is evaluated first.

## Precedence Table

1. `**` (Exponentiation)
2. `*`, `/`, `//`, `%` (Multiplication, Division, Floor Division, Modulus)
3. `+`, `-` (Addition, Subtraction)

Let's take a more complex example:

```python
>>> 3 ** 2 * 4 - 4
32
```

Here, the exponentiation (`**`) is performed first:

```python
(3 ** 2) * 4 - 4
(9) * 4 - 4
36 - 4
32
```

## Order of Evaluation (Left-to-Right)

Most operators are evaluated from **left to right**, except for the exponentiation (`**`) and assignment (`=`) operators, which are evaluated from **right to left**.

For example:

```python
>>> 3 - 2 + 1
2
```

This evaluates as:

```python
(3 - 2) + 1 = 1 + 1 = 2
```

Another example with modulus (`%`):

```python
>>> 8 % 4 % 2
0
```

Evaluated as:

```python
(8 % 4) % 2 = 0 % 2 = 0
```

However, exponentiation works differently:

```python
>>> 2 ** 3 ** 0
2
```

This is evaluated from **right to left**:

```python
2 ** (3 ** 0) = 2 ** 1 = 2
```

---

## Boolean Expressions: Precedence and Order

### Basic Boolean Expressions

A simple boolean expression evaluates to `True` or `False`:

```python
>>> 1 > 0
True
```

You can combine multiple conditions using logical operators like `and` and `or`:

```python
>>> 3 < 3.14 < 4
True
```

### Precedence and Order of Logical Operators

Similar to arithmetic operators, logical operators follow precedence rules:

1. `not` (negation)
2. `and` (conjunction)
3. `or` (disjunction)

Logical expressions are evaluated from **left to right**, but operator precedence affects the order.

For example:

```python
>>> not True and False
False
```

The precedence of `not` is higher than `and`, so it's evaluated as:

```python
(not True) and False = False and False = False
```

Another example:

```python
>>> True or False and False
True
```

Here, `and` has higher precedence than `or`, so it's evaluated as:

```python
True or (False and False) = True or False = True
```

---

## Beware of Float Comparisons

Be cautious when comparing floats, as Python uses approximations to represent floating-point numbers. For example:

```python
>>> 10.00000000000000000000001 > 10
False
```

This is because the float precision rounds the number to `10.0`.

```python
>>> 0.1 * 3 == 0.3
False
>>> 0.1 * 3
0.30000000000000004
```

---

## Short Circuit Evaluation

Python uses **short circuit evaluation** to optimize boolean expressions. If the outcome of a logical operation can be determined by the first operand, the second operand is not evaluated.

For example:

```python
>>> True or (1 / 0)
True
```

No error occurs because Python doesn't evaluate `(1 / 0)` once it determines that the expression is `True`.

This behavior applies to `and` as well. If the first operand is `False`, the second operand isn't evaluated:

```python
>>> False and (1 / 0)
False
```

This makes short circuit evaluation useful in avoiding errors in complex expressions.
