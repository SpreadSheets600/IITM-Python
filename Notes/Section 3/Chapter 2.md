# Loops in Python

## `for` Loop

Let us look at a simple problem of printing numbers. We would like to print the first 5 non-negative integers using a `for` loop:

### Code

```python
for i in range(5):
    print(i)
# A dummy line
```

### Output

```python
0
1
2
3
4
```

In this example:

- `for` and `in` are keywords in Python.
- `range` is an object that represents a sequence of numbers.
- Line 2 is the body of the loop.

### Understanding the Code

- In each iteration of the loop, an element in the sequence is picked up and printed to the console.
- The sequence is processed from left to right.
- Once the rightmost element has been printed, control returns to line 1 for one last time. Since there are no more elements to read in the sequence, the control exits the loop.

### Visual Representation

![For Loop Visual Representation](path/to/visual_representation.png)

Similar to `while` loops and `if-else` blocks, the body of a `for` loop should be indented.

---

## `range()`

The `range(5)` function represents the following sequence: `0, 1, 2, 3, 4`. In general, `range(n)` represents the sequence: `0, 1, ..., n - 1`.

The `range` function is quite versatile. For example, the following code prints all two-digit numbers greater than zero:

### Code

```python
for i in range(10, 100):
    print(i)
```

`range(10, 100)` represents the sequence `10, 11, ..., 99`. In general, `range(start, stop)` represents the sequence `start, start + 1, ..., stop - 1`.

### Example: Even Two-Digit Numbers

Let us add another level of complexity. The following code prints all even two-digit numbers greater than zero:

### Code

```python
for i in range(10, 100, 2):
    print(i)
```

`range(10, 100, 2)` represents the sequence `10, 12, ..., 98`. In general, `range(start, stop, step)` represents the sequence `start, start + step, start + 2 * step, ..., last`, where `last` is the largest element in this sequence that is less than `stop`. This is true when the step parameter is positive.

### Equivalents

The following are equivalent:

- `range(n)`
- `range(0, n)`
- `range(0, n, 1)`

### Decreasing Sequences

So far, we have seen only increasing sequences. With the help of a negative step size, we can also come up with decreasing sequences. The following code prints all two-digit even numbers greater than zero in descending order:

### Code

```python
for i in range(98, 9, -2):
    print(i)
```

For a negative step value, `range(start, stop, step)` represents the sequence `start, start + step, start + 2 * step, ..., last`, where `last` is the smallest element in the sequence greater than `stop`.

### Empty Sequences

Now, consider the following code:

### Code

```python
for i in range(5, 5):
    print(i)
```

`range(5, 5)` is an empty sequence, so the above code will not print anything.

Another instance of an empty sequence:

### Code

```python
for i in range(10, 5):
    print(i)
```

Neither of these snippets produces any error.

```python
for i in range(0.0, 10.0):
    print(i)
```

---

## Iterating through Strings

Since a string is a sequence of characters, we can use the `for` loop to iterate through strings. The following code will print each character of the string `x` in one line:

### Code

```python
word = 'good'
for char in word:
    print(char)
```

### Output

```python
g
o
o
d
```

We can add some more code to enrich the output:

### Code

```python
word = 'good'
count = 1
for char in word:
    print(char, 'occurs at position', count, 'in the string', word)
    count = count + 1
```

### Output

```python
g occurs at position 1 in the string good
o occurs at position 2 in the string good
o occurs at position 3 in the string good
d occurs at position 4 in the string good
```
