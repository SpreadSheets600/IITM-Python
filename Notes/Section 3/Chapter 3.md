# Nested Loops in Python

## Problem: Finding Ordered Pairs

Consider the following problem:

**Find the number of ordered pairs of positive integers whose product is 100.** Note that order matters: (2, 50) and (50, 2) are two different pairs.

### Solution

```python
count = 0
for a in range(1, 101):
    for b in range(1, 101):
        if a * b == 100:
            count = count + 1
print(count)
```

The code above is an example of a nested loop. Lines 2-5 form the outer loop while lines 3-5 form the inner loop. There are multiple levels of indentation here:

- Line 3 begins a new `for` loop.
- Line 4 is indented with respect to line 3.
- Line 5 is indented with respect to line 4.

This problem could have been solved without using a nested loop. The nested loop is not an efficient solution. It is left as an exercise to the reader to come up with a more efficient solution to this problem.

---

## Problem: Counting Prime Numbers

**Find the number of prime numbers less than n, where n is some positive integer.**

### Solution

```python
n = int(input())
count = 0
for i in range(2, n + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        count = count + 1
print(count)
```

### Explanation

The basic idea behind the solution is as follows:

1. The outer `for` loop goes through each element in the sequence 2, 3, ..., n. `i` is the loop variable for this sequence.
2. We begin with the guess that `i` is prime. In code, we do this by setting `flag` to be `True`.
3. Now, we go through all potential divisors of `i`. This is represented by the sequence 2, 3, ..., `i - 1`. Variable `j` is the loop variable for this sequence. Notice how the sequence for the inner loop is dependent on `i`.
4. If `j` divides `i`, then `i` cannot be prime. We correct our initial assumption by updating `flag` to `False` whenever this happens. If `j` doesn't divide `i` for any `j`, then `i` is prime, and `flag` stays `True`.
5. Once we are outside the inner loop, we check if `flag` is `True`. If that is the case, then we increment `count`, as we have hit upon a prime number.

### Important Points About Nested Loops

- Nesting is not restricted to `for` loops. Any of the following combinations are possible:
  - `for` inside `for`
  - `for` inside `while`
  - `while` inside `while`
  - `while` inside `for`
- Multiple levels of nesting are possible.

---

## While vs. For Loops

`for` loops are typically used in situations where the number of iterations can be quantified, while `while` loops are used when the number of iterations cannot be quantified exactly.

### Example: For Loop

```python
n = int(input())
for i in range(n):
    print(i ** 2)
```

In this code, the number of iterations varies each time the code is run with a different input. However, given the knowledge of the input, the number of iterations is fixed.

### Example: While Loop

```python
x = int(input())
while x > 0:
    x = int(input())
```

In this case, the number of iterations can only be determined after it terminates. There is no way to quantify the number of iterations as an explicit function of user input.

---

## Print Function: `end` and `sep`

### Problem: Printing Numbers from 1 to n

Accept a positive integer `n` as input and print all the numbers from 1 to `n` in a single line separated by commas.

For a given value of `n`, say `n = 9`, we want the output to be:

```
1,2,3,4,5,6,7,8,9
```

### Solution

```python
n = int(input())
for i in range(1, n + 1):
    print(i, end=',')
print(n)
```

For `n = 9`, this will give the required output:

```
1,2,3,4,5,6,7,8,9
```

The print function's default behavior is to append a newline after each output. By using the `end` argument, we can change this behavior.

### Example of `end`

```python
print()
print(end=',')
print(1)
print(1, end=',')
print(2, end=',')
print(3, end=',')
```

**Output:**

```
,1
1,2,3,
```

### Separator with `sep`

If multiple expressions are passed to the print function, it prints all of them in the same line, adding a space between adjacent expressions.

#### Example:

```python
print('this', 'is', 'cool')
```

**Output:**

```
this is cool
```

If we do not want the space or want a different separator, we can use `sep`:

```python
print('this', 'is', 'cool', sep=',')
```

**Output:**

```
this,is,cool
```

We could also have an empty string as the separator:

```python
print('this', 'is', 'cool', sep='')
```

**Output:**

```
thisiscool
```

---

## Using `end` and `sep` Together

### Problem: Print Pattern

Accept a positive integer `n`, which is also a multiple of 3, as input and print the following pattern:

```
|1,2,3|4,5,6|7,8,9|...|n - 2,n - 1,n|
```

For `n = 9`, we would like to print:

```
|1,2,3|4,5,6|7,8,9|
```

### Solution

```python
n = int(input())
print('|', end='')
for i in range(1, n + 1, 3):
    print(i, i + 1, i + 2, sep=',', end='|')
print()
```

Notice that the `for` loop iterates in steps of 3 starting from 1. To print the comma-separated triplet `i,i + 1,i + 2`, `sep` is set to `,`. After printing each triplet, the symbol `|` is printed by setting `end` to `|`. The last print statement ensures the prompt moves to the next line once the pattern is printed. You can try removing the last line and see how that changes the output.
