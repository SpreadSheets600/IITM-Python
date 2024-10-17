# Loops in Python

## Introduction

Consider the following problem:

### Problem

Print the sum of the first five positive integers.

### Solution

```python
print(1 + 2 + 3 + 4 + 5)
```

Now, how about the following problem?

### Problem

Print the sum of the first 1,000,000 positive integers.

The earlier approach is not going to work. If it takes about five seconds on average to write a number followed by the `+` symbol, how much time will it take to find the sum of all 1 million numbers? Let us check:

### Code

```python
num = 1_000_000     # _ in a number is used when we have large numbers; improves readability
avg_time = 5
seconds = num * avg_time
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
print('Approximate number of days =', round(days))
```

It will take nearly 58 days to sum all 1 million integers! This is assuming that we work like machines that don't need food or sleep. All of this just to do something as trivial as finding the sum of numbers. This is where loops come in.

---

## `while` Loops

The "loopy" solution to this problem:

### Code

```python
total = 0
num = 0
while num < 1_000_000:
    num = num + 1
    total = total + num
print(total)
```

The `while` keyword is used in Python to create a loop. The expression adjacent to `while` is a boolean expression, called the **while-condition**. Lines 4 and 5 make up the body of the `while` loop. If the condition evaluates to `True`, control enters the body of the `while`. The lines in the body are sequentially executed. After the last line in the body is executed, the control loops back to the condition evaluation. As long as the condition is `True`, the body of the `while` keeps getting executed. The moment the condition becomes `False`, the body of the `while` is skipped, and control transfers to the next line. The body of the `while` loop must always be indented; this helps to separate it from the rest of the code.

### Visual Representation

![While Loop Visual Representation](path/to/visual_representation.png)

Let us consider another example:

### Problem

Keep accepting integers as input from the user until the user enters a negative number. Print the sum of the positive numbers entered by the user. Print `0` if the user doesn't enter any positive integer.

### Code

```python
total = 0
num = int(input())
while num >= 0:
    total += num
    num = int(input())
print(total)
```

---

## Another Example

### Problem

Keep accepting integers as input from the user until the user enters a negative number. Print the maximum among the positive numbers entered by the user. Print `0` if the user doesn't enter any positive integer.

### Solution

```python
# Initialize
num = int(input())
max_num = 0
# Loop
while num >= 0:
    if num > max_num:
        max_num = num
    num = int(input())
# Print output
print(max_num)
```

Note that lines 6-8 make up the body of the `while` loop and are indented. Lines 1, 4, and 9 have comments to help the reader understand what is happening in the code.

---

## `break` and `continue`

The `break` and `continue` keywords are associated with loops in Python.

### `break`

The `break` statement is used to exit out of a loop without executing any code that comes below it. For example:

### Code

```python
num = 1
while True:
    if (num % 2 == 0) and (num % 3 == 0) and (num % 4 == 0):
        break
    num = num + 1
print(num)
```

The above code prints the smallest positive integer that is divisible by `2`, `3`, and `4`, which is the same as the LCM of `(2, 3, 4)`. The moment this number is found, the code breaks out of the loop.

### `continue`

The `continue` statement is used to move to the next iteration of the loop, skipping whatever code comes below it. For example:

### Code

```python
x = 0
while x < 50:
    x = x + 1
    if x % 3 != 0:
        continue
    print(x)
```

The code given above prints all positive integers less than or equal to `50` that are divisible by `3`. Whenever `x` is not divisible by `3`, we do not want to print the number, so we continue to the next iteration.
