## Arguments

Python offers various options for how arguments can be passed to functions. Each method of argument passing addresses the following question:

**How are the arguments in the function call passed to the parameters in the function definition?**

### Positional Arguments

All functions that we have seen so far use positional arguments. Here, the position of an argument in the function call determines which parameter it is passed to. For example:

**Problem**: Write a function that accepts three positive integers \( x \), \( y \), and \( z \). Return `True` if the integers form the sides of a right triangle with \( x \) and \( y \) as the legs and \( z \) as the hypotenuse, and `False` otherwise.

**Solution**:

```python
def isRight(x, y, z):
    if x ** 2 + y ** 2 == z ** 2:
        return True
    return False

print(isRight(3, 4, 5))  # 3 is passed to x, 4 to y, 5 to z
print(isRight(5, 4, 3))  # 5 is passed to x, 4 to y, 3 to z
```

**Output**:

```
True
False
```

Arguments are passed to the parameters based on their position in the function call. Positional arguments are also known as required arguments; they cannot be omitted. Attempting to provide more arguments than there are parameters will result in an error. For example, executing the following code will produce an error:

```python
# Alarm! Wrong code snippet!
isRight(3, 4)
isRight(3, 4, 5, 6)
# Alarm! Wrong code snippet!
```

### Keyword Arguments

Keyword arguments introduce more flexibility in passing arguments. Consider the same problem from above, modified to use keyword arguments:

```python
# The following is just a function call.
# We are not printing anything here.
isRight(x=3, y=4, z=5)
```

In this call, the names of the parameters are explicitly specified, and the arguments are assigned using the `=` operator. This differs from positional arguments, where the position in the call determines the parameter. An advantage of keyword arguments is that they reduce the likelihood of incorrect order. For example:

```python
isRight(3, 4, 5)          # Intended call
isRight(5, 4, 3)          # Actual call
isRight(x=3, y=4, z=5)    # Same as intended call
isRight(z=5, y=4, x=3)    # Same as intended call
```

Positional and keyword arguments can be combined in a single call:

```python
isRight(3, y=4, z=5)
```

However, you cannot do the following:

```python
# Alarm! Wrong code snippet!
isRight(x=3, 4, 5)
# Alarm! Wrong code snippet!
```

The interpreter throws a `TypeError`: "positional argument follows keyword arguments." When both types are present, keyword arguments must come last.

Consider this call:

```python
# Alarm! Wrong code snippet!
isRight(3, x=3, y=4, z=5)
# Alarm! Wrong code snippet!
```

This will throw a `TypeError`: "isRight() got multiple values for argument x." Only one argument can be passed for each parameter in the function definition, whether positional or default, but not both.

### Default Arguments

Let’s consider a scenario with two distance metrics: Euclidean and Manhattan. Assume a self-driving car startup uses these metrics repeatedly in its code base. You can represent them as functions:

```python
def euclidean(x, y):
    return pow(x ** 2 + y ** 2, 0.5)

def manhattan(x, y):
    return abs(x) + abs(y)
```

However, since the Manhattan distance is used more frequently, default arguments can help streamline the function:

```python
def distance(x, y, metric='manhattan'):
    if metric == 'manhattan':
        return abs(x) + abs(y)
    elif metric == 'euclidean':
        return pow(x ** 2 + y ** 2, 0.5)
```

In this case, the `metric` parameter has a default value of `'manhattan'`. If we call the function without specifying this parameter:

```python
print(distance(3, 4))
```

This outputs `7`, as the default value of `'manhattan'` is used.

Key points regarding default parameters:

- Parameters assigned a value in the function definition are called default parameters.
- Default parameters must always be at the end of the parameter list.
- Arguments for default parameters are optional in a function call.
- Arguments for default parameters can be passed as positional or keyword arguments.

Here are examples of valid function calls with default parameters:

```python
distance(3, 4)
distance(3, 4, 'manhattan')
distance(3, 4, metric='manhattan')
```

All three calls are equivalent.

### Call by Value

Consider the following code:

```python
def double(x):
    x = x * 2
    return x

a = 4
print(f'before function call, a = {a}')
double(a)
print(f'after function call, a = {a}')
```

**Output**:

```
before function call, a = 4
after function call, a = 4
```

Here, the value of `a` remains unchanged after the function call. When `double(a)` is invoked, the value in `a` is assigned to the parameter `x` in the function. This kind of function call, where the value of a variable is passed as an argument, is called **call by value**.

Now consider this example:

```python
def square(x):
    return x * x

x = 10
x_squared = square(x)
```

Using the same name for both the parameter of the function and the argument passed is not advisable. It’s better to differentiate the names to avoid confusion and improve code readability. The above code could be rewritten as follows:

```python
def square(num):
    return num * num

x = 10
x_squared = square(x)
```
