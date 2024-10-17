# Variables

## Introduction

Variables are containers used to store values. In Python, variables are defined using the assignment operator `=`. For example:

```python
x = 1
y = 100.0
z = "good"
```

Variables can also be updated using the assignment operator:

```python
x = 1
print('The initial value of x is', x)
x = 2
print('The value after updating x is', x)
```

The output is:

```python
The initial value of x is 1
The value after updating x is 2
```

---

## Assignment Operator

The syntax of the assignment statement is:

```python
<variable-name> = <expression>
```

The assignment operator works from right to left. For example:

```python
x = 1 + 2 * 3 / 2
print(x)
```

The output is:

```python
4.0
```

Having a literal to the left of the assignment operator will result in an error:

```python
3 = x
```

This will throw the following error:

```python
SyntaxError: cannot assign to literal
```

---

## Dynamic Typing

Python supports dynamic typing. In a dynamically typed language, a variable is simply a value bound to a name; the value has a type — like `int` or `str` — but the variable itself doesn’t. For example:

```python
a = 1
print(type(a))
a = 1 / 2
print(type(a))
```

The output is:

```python
<class 'int'>
<class 'float'>
```

---

## Referencing vs Defining

When a variable that has already been defined is used in an expression, we say that the variable is being _referenced_.

```python
x = 2
print(x * x, 'is the square of', x)
```

If a variable is referenced before it has been assigned a value, Python throws a `NameError`:

```python
print(someVar)
```

The output is:

```python
NameError: name 'someVar' is not defined
```

---

## Keywords and Naming Rules

Certain words in Python, called **keywords**, have special meanings. Examples include:

```python
not, and, or, if, for, while, in, is, def, class
```

Keywords cannot be used as variable names:

```python
and = 2
```

In addition to this restriction, variable names in Python must follow these rules:

1. A variable name can only contain alphanumeric characters and underscores: `a-z`, `A-Z`, `0-9`, `_`
2. A variable name must start with a letter or an underscore.
3. Variable names are case-sensitive (`age`, `Age`, and `AGE` are three different variables).

---

## Reusing Variables

Variables can be used in computing the values of other variables. For example:

```python
x = 10
y = x ** 2
z = (x + 1) * (y + 1)
```

---

## Multiple Assignment

You can assign values to multiple variables in one line:

```python
x, y = 1, 2
```

Another way is to assign the same value to multiple variables:

```python
x = y = z = 10
```

Even though `x`, `y`, and `z` start off equal, the equality is broken if one of them is updated:

```python
x = x * 1
y = y * 2
z = z * 3
print(x, y, z)
```

The output is:

```python
10 20 30
```

---

## Assignment Shortcuts

Python provides shorthand notations for arithmetic operations combined with assignment:

| Shortcut  | Meaning      |
| --------- | ------------ |
| `x += a`  | `x = x + a`  |
| `x -= a`  | `x = x - a`  |
| `x *= a`  | `x = x * a`  |
| `x /= a`  | `x = x / a`  |
| `x %= a`  | `x = x % a`  |
| `x **= a` | `x = x ** a` |

For example:

```python
x = 1
x += 1
print(x)
```

The output is:

```python
2
```

---

## Deleting Variables

You can delete variables using the `del` keyword:

```python
x = 100
print('x is a variable whose value is', x)
print('we are now going to delete x')
del x
print(x)
```

After the deletion, trying to access `x` will throw a `NameError`:

```python
NameError: name 'x' is not defined
```
