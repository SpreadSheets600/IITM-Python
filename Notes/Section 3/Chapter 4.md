# Formatted Printing

Consider the following program:

```python
name = input()
print('Hi,', name, '!')
```

When this code is executed with `Sachin` as the input, we get the following output:

```
Hi, Sachin !
```

This looks messy as there is an unwanted space after the name. This is a formatting issue. Python provides some useful tools to format text the way we want.

---

## f-strings

The first method we will look at is called formatted string literals, or _f-strings_ for short. Let us jump into the syntax:

```python
name = input()
print(f'Hi, {name}!')
```

When this code is executed with `Sachin` as the input, we get the following output:

```
Hi, Sachin!
```

The messy formatting has been corrected. Let us take a closer look at the string inside the print command:

```python
f'Hi, {name}'
```

This is called a formatted string literal, or _f-string_. The `f` in front of the string differentiates f-strings from normal strings. An f-string is an object that, when evaluated, results in a string. The value of the variable `name` is inserted in place of `{name}` in the f-string.

Two things are important for f-strings to work correctly:

1. The `f` in front of the string.
2. The curly braces `{}` enclosing the variable.

Let us see what happens if we miss one of these two:

```python
name = 'Sachin'
print('Hi, {name}!')
print(f'Hi, name!')
```

This will give the output:

```
Hi, {name}!
Hi, name!
```

Let us now look at a few other examples:

```python
l, b = int(input()), int(input())
print(f'The length of the rectangle is {l} units')
print(f'The breadth of the rectangle is {b} units')
print(f'The area of the rectangle is {l * b} square units')
```

For `l = 4`, `b = 5`, the output is:

```
The length of the rectangle is 4 units
The breadth of the rectangle is 5 units
The area of the rectangle is 20 square units
```

Notice that line-4 has an expression — `l * b` — inside the curly braces, not just a variable. f-strings allow any valid Python expression inside the curly braces. If the f-string has some `{expression}` in it, the interpreter will substitute the value of the expression.

Another example:

```python
x = int(input())
print(f'Multiplication table for {x}')
for i in range(1, 11):
    print(f'{x} X {i} \t=\t {x * i}')
```

For an input of `3`, this will give the following result:

```
Multiplication table for 3
3 X 1   =    3
3 X 2   =    6
3 X 3   =    9
3 X 4   =    12
3 X 5   =    15
3 X 6   =    18
3 X 7   =    21
3 X 8   =    24
3 X 9   =    27
3 X 10  =    30
```

The `\t` is a tab character. It has been added before and after the `=`. Remove both tabs and run the code to observe any changes in the output.

Till now, we have used f-strings within the `print` statement. Nothing stops us from using them to define other string variables:

```python
name = input()
qual = input()
gender = input()
if qual == 'phd':
    name_respect = f'Dr. {name}'
elif gender == 'male':
    name_respect = f'Mr. {name}'
elif gender == 'female':
    name_respect = f'Ms. {name}'
print(f'Hello, {name_respect}')
```

Try to guess what this code is doing.

---

## `format()`

Another way to format strings is by using a string method called `format()`.

```python
name = input()
print('Hi, {}!'.format(name))
```

In the above string, the curly braces `{}` will be replaced by the value of the variable `name`. Another example:

```python
l, b = int(input()), int(input())
print('The length of the rectangle is {} units'.format(l))
print('The breadth of the rectangle is {} units'.format(b))
print('The area of the rectangle is {} square units'.format(l * b))
```

Let us now print the multiplication table using `format`:

```python
x = int(input())
for i in range(1, 11):
    print('{} X {} \t=\t {}'.format(x, i, x * i))
```

The output will be identical to the one we saw with f-strings.

---

## Format Specifiers

Consider the following code:

```python
pi_approx = 22 / 7
print(f'The value of pi is approximately {pi_approx}')
```

This gives the following output:

```
The value of pi is approximately 3.142857142857143
```

There are too many numbers after the decimal point. Format specifiers are a way to solve this problem:

```python
pi_approx = 22 / 7
print(f'The value of pi is approximately {pi_approx:.2f}')
```

This gives the following output:

```
The value of pi is approximately 3.14
```

### Example

Let us print the marks of three students in a class with right alignment:

```python
roll_1, marks_1 = 'BSC1001', 90.5
roll_2, marks_2 = 'BSC1002', 100
roll_3, marks_3 = 'BSC1003', 90.15
print(f'{roll_1}: {marks_1:10.2f}')
print(f'{roll_2}: {marks_2:10.2f}')
print(f'{roll_3}: {marks_3:10.2f}')
```

This produces the output:

```
BSC1001:      90.50
BSC1002:     100.00
BSC1003:      90.15
```

The `10.2f` in `{marks_1:10.2f}` specifies that the float should be rounded to two decimal places, with a minimum width of 10.

Another example with integers:

```python
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{:5d}'.format(1111))
print('{:5d}'.format(11111))
print('{:5d}'.format(111111))
```

This gives the following output:

```
    1
   11
  111
 1111
11111
111111
```

### Points to Note

- `d` stands for integer.
- `5d` after `:` specifies a minimum column width of 5.
