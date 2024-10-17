# Library in Python

A library is a collection of functions that share a common theme. This loose definition will become clear when we start working with a library.

## Using the `calendar` Library

Consider the following problem:

### Problem

In the year 3000, which day of the week will August 15th fall on?

### Solution

```python
import calendar
calendar.prmonth(3000, 8)
```

### Output

When the above code is executed, the output is:

```python
    August 3000
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```

15th of August falls on a Friday. Isn't that lovely? It took just two lines of code!

The `calendar` library is one among several libraries in Python's standard library. A comprehensive list can be found [here](https://docs.python.org/3/library/index.html).

In the code, `calendar` is the name of the library and `import` is the keyword used to include this library as part of the code. The `calendar` library is a collection of functions that are related to calendars. The `prmonth` function accepts `<year>` and `<month>` as input and displays the calendar for that month in the specified year.

#### Note

If we skip the import step:

```python
# import calendar
calendar.prmonth(3000, 8)
```

It gives the following error:

```python
NameError: name 'calendar' is not defined
```

To access a function defined inside a library, we use the following syntax:

```python
<library>.<function>(<arguments>)
```

### Alternative Solution

Another way to solve the problem is to use the `weekday` function:

```python
import calendar
print(calendar.weekday(3000, 8, 15))
```

### Output

The output of the above code is `4`, which means:
| Day | Number |
|-----------|--------|
| Monday | 0 |
| Tuesday | 1 |
| Wednesday | 2 |
| Thursday | 3 |
| Friday | 4 |
| Saturday | 5 |
| Sunday | 6 |

---

## Using the `time` Library

Let us now try to answer this hypothetical question:

### Problem

You are stranded on an island in the middle of the Indian Ocean. The island has a computing device that has just one application installed in it: a Python interpreter. You wish to know the current date and time.

### Solution

```python
from time import ctime
print('The current time is:', ctime())
```

### Output

```python
The current time is: Fri Apr  2 12:24:43 2021
```

The syntax of the import statement in line-1 looks different. The `from` keyword allows us to import a specific function from a library.

This way of importing functions is useful when we need just one or two functions from a given library:

```python
from time import ctime, sleep
print('Current time is:', ctime())
print('I am going to sleep for 10 seconds')
sleep(10)
print('Current time is:', ctime())
```

The `sleep(x)` function in the `time` library suspends the execution of the program for `x` seconds. If we would be using several functions in the library, it is better to import the entire library.

---

## The Zen of Python

As a fun exercise, consider the following code:

```python
import this
```

### Output

This gives the following output:

```python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

These are some nuggets of wisdom from Tim Peters, a "major contributor to the Python programming language". Some points make immediate sense, such as "readability counts".
