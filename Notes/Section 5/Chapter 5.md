# Tuples

## Introduction

A tuple is an immutable sequence of values:

```python
family = ('father', 'mother', 'child')
print(type(family))  # <class 'tuple'>
print(isinstance(family, tuple))  # True
```

Tuples resemble lists in that they can be indexed and sliced:

```python
print(family[0])  # 'father'
print(family[:2])  # ('father', 'mother')
```

The key difference between lists and tuples is that tuples cannot be updated in-place due to their immutability. Therefore, the following operation will raise an error:

```python
##### Alarm! Wrong code snippet! #####
numbers = ('one', 'two', 'four')
numbers[2] = 'three'  # TypeError: 'tuple' object does not support item assignment
##### Alarm! Wrong code snippet! #####
```

As a result, elements in a tuple cannot be appended, inserted, or deleted. The only methods defined for tuples are `count` and `index`, which function as expected:

```python
numbers = (1, 2, 3, 1, 1)
print(numbers.count(1))  # 3
print(numbers.index(2))  # 1
```

We can iterate through a tuple using a for loop:

```python
for num in (1, 2, 3):
    print(num)
```

Since tuples are immutable, they are passed by value in functions, similar to other immutable types like strings and numbers. Useful functions for tuples include `sum`, `max`, and `min`.

---

## More on Tuples

Here are some additional points about tuples:

- A singleton tuple should be defined with a comma:

```python
i_am_single = (1,)
print(len(i_am_single))  # 1
print(isinstance(i_am_single, tuple))  # True
```

If the comma is removed:

```python
i_am_single = (1)
print(isinstance(i_am_single, int))  # True
```

- A list can be converted into a tuple, and vice versa:

```python
a_list = [1, 2, 3]
a_tuple = tuple(a_list)  # (1, 2, 3)
b_tuple = (1, 2, 3)
b_list = list(b_tuple)  # [1, 2, 3]
```

- A tuple can hold a non-homogeneous sequence of items:

```python
a_tuple = (1, 'cool', True)
```

- Membership can be checked using the `in` keyword:

```python
1 in (1, 2, 3)  # True
'hello' not in ('some', 'random', 'sequence')  # True
```

- Tuples can be nested:

```python
a = ((1, 2, 3), (4, 5, 6))
print(a[0][2])  # 3
```

- A tuple can hold mutable objects:

```python
a_tuple = ([0, 1, 2], [4, 5, 6])
a_tuple[0][0] = 100  # Runs without error
```

Although `a_tuple` is immutable, the elements inside it are mutable. We can verify that the identity of the element remains unchanged:

```python
a_tuple = ([0, 1, 2], [4, 5, 6])
print(id(a_tuple[0]))  # ID of the first element
a_tuple[0][0] = 100
print(id(a_tuple[0]))  # Same ID as before
```

This shows that while the values inside mutable objects can change, their identities remain the same.

---

## Lists and Tuples Comparison

Here’s a brief summary highlighting the similarities and differences between lists and tuples:

| List                                                                                 | Tuple                               |
| ------------------------------------------------------------------------------------ | ----------------------------------- |
| Mutable                                                                              | Immutable                           |
| `L = [1, 2, 3]`                                                                      | `T = (1, 2, 3)`                     |
| Supports indexing and slicing                                                        | Supports indexing and slicing       |
| Supports item assignment                                                             | Doesn't support item assignment     |
| Supported methods: `count`, `index`, `append`, `insert`, `remove`, `pop`, and others | Supported methods: `count`, `index` |
| To get a list: `list(obj)`                                                           | To get a tuple: `tuple(obj)`        |

The relationship between lists and tuples can be further illustrated with an example of populating a list with ordered pairs of positive integers whose product is 100:

```python
pairs = []
for a in range(1, 101):
    for b in range(1, 101):
        if a * b == 100:
            pairs.append((a, b))
print(pairs)
```

Here, `pairs` is a list of tuples. Using tuples is preferable because the two elements in each pair have a well-defined relationship, and we want to avoid accidental modifications.

---

## Packing and Unpacking

Despite seeming redundant, tuples play a significant role in Python. For example:

```python
T = 1, 2, 3
print(T)  # (1, 2, 3)
print(isinstance(T, tuple))  # True
```

This is an example of **tuple packing** where the values 1, 2, and 3 are packed into a tuple. The reverse operation, **sequence unpacking**, is demonstrated as follows:

```python
x, y, z = T
print(x, y, z)  # 1 2 3
```

Multiple assignment combines tuple packing and sequence unpacking:

```python
x, y, z = 1, 2, 3  # Packs (1, 2, 3) and unpacks to x, y, z
```

Any sequence can be unpacked:

```python
l1, l2, l3, l4 = 'good'  # string
num1, num2, num3 = [1, 2, 3]  # list
b1, b2 = (True, False)  # tuple
x, y, z = range(3)  # range
```

This functionality also applies when multiple values are returned from functions:

```python
def max_min(a, b):
    if a > b:
        return a, b
    return b, a

x = max_min(1, 2)
print(x)  # (2, 1)
print(isinstance(x, tuple))  # True
```

In the return statements, the multiple values are packed into a tuple, demonstrating how functions can return tuples.
