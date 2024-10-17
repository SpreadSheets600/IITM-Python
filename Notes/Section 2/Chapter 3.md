# Conditional Statements

## if Statement

Let's explore the idea of conditional statements by solving a simple problem:

### Problem

Accept an integer as input from the user. If the number is greater than or equal to zero, print: **non-negative**.

### Solution

```python
x = int(input())
if x >= 0:
    print('non-negative')
```

The `if` is a keyword in Python. The expression next to `if` is a boolean expression, also called the if-condition or just the condition. The body of the if statement is indented, indicating which lines are to be executed if the condition evaluates to True.

The following diagram captures the control flow of the `if` statement:

![if Statement Flowchart](link_to_if_flowchart)

### Code Snippet

```python
x = int(input())
if x >= 0:
    print('non-negative')
```

Note that line-3 in the solution code is indented. In this case, the indentation corresponds to four spaces, and it's crucial to keep this consistent throughout the program.

### Example

To understand how indentation works, consider the following code blocks:

#### Left

```python
x = 1
if x >= 0:
    print('non-negative')
    print('inside if')
print('outside if')
```

#### Right

```python
x = -1
if x >= 0:
    print('non-negative')
    print('inside if')
print('outside if')
```

**Output**:

- Left:

  ```python
  non-negative
  inside if
  outside if
  ```

- Right:
  ```python
  outside if
  ```

Lines 3-5 in the left code make up the if-block. Whenever the if-condition evaluates to True, the interpreter executes the body of the if.

---

## if-else Statement

Let's add another level of complexity to the problem.

### Problem

Accept an integer as input from the user. If the number is greater than or equal to zero, print: **non-negative**. If the number is less than zero, print **negative**.

### Solution

```python
x = int(input())
if x >= 0:
    print('non-negative')
else:
    print('negative')
```

`else` is another keyword in Python. When the `if` condition is True, the statements inside the if block are executed. When the condition is False, the statements inside the else block are executed.

### Points to Remember

- `if` and `else` must be at the same level of indentation.
- `else` cannot exist independently of an `if` statement.
- `else` cannot have a condition associated with it.

---

## if-elif-else Statement

Time for another bump in complexity.

### Problem

Accept an integer as input from the user. If the number is greater than zero, print: **positive**. If the number is less than zero, print **negative**. If the number is equal to zero, print **zero**.

### Solution

```python
x = int(input())
if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')
```

`elif` is a shorthand for else-if.

### Example Inputs and Outputs

| Input  | Output   |
| ------ | -------- |
| x = 1  | positive |
| x = 0  | zero     |
| x = -1 | negative |

The general syntax for `if-elif-else` is:

```python
if <condition-1>:
    <statement-1>
elif <condition-2>:
    <statement-2>
else:
    <statement-3>
```

**Features to Note**:

- Exactly one of the three statements gets executed.
- If an `if` or `elif` condition evaluates to True, the body of that block is executed, and the flow exits the entire if-elif-else block.
- There can be multiple `elif` conditions after the `if`.

---

## Nested Conditional Statements

Consider the following problem:

### Problem

Accept three distinct integers as input from the user. If the numbers have been entered in ascending order, print **in ascending order**. If not, print **not in ascending order**.

### Incomplete Solution

```python
x = int(input())
y = int(input())
z = int(input())

if x < y:
    print('in ascending order')
else:
    print('not in ascending order')
```

The issue with this solution is that it doesn't check if `y < z`. The complete solution is given below:

### Complete Solution

```python
x = int(input())
y = int(input())
z = int(input())

if x < y:
    if y < z:
        print('in ascending order')
    else:
        print('not in ascending order')
else:
    print('not in ascending order')
```

### Indentation

Whenever a new if block is introduced, its body should have exactly one level of indentation with respect to its if-condition.

---

## Defining Variables Inside if

Consider the following snippet of code:

```python
x = int(input())
if x % 5 == 0:
    output = 'the number is divisible by 5'
print(output)
```

### Observation

Run the code multiple times, varying the input each time. When the input is a multiple of 5, the code runs without any error. However, when the input is not divisible by 5, the code throws a `NameError` because the variable `output` is referenced even when it has not been defined.
