### Scope

- **Definition**: The scope of a variable determines where it can be accessed or modified in the code.
- **Local Scope**: Variables defined inside a function (like `x` in `foo()`) are local to that function and cannot be accessed from outside it. Attempting to do so will raise a `NameError`.
- **Global Scope**: Variables defined outside any function (like `y` in the second example) can be accessed within functions as long as they are defined before the function call. If a variable is only referenced and not assigned within a function, it is treated as global.

### Local vs Global Variables

- **Local Variables**: Assigned within a function. If you create a variable inside a function, it only exists there.
- **Global Variables**: Can be referenced anywhere in the code after being defined. However, if you define a variable with the same name inside a function, it will shadow the global variable.

### Example Analysis

1. **Local Variable Example**:

   ```python
   def foo():
       x = 1
       print(x)  # Works fine
   foo()
   print(x)  # Raises NameError
   ```

   In this case, `x` is local to `foo()`.

2. **Global Variable Example**:

   ```python
   y = 10
   def foo():
       print(y)  # Works fine, y is global
   foo()
   ```

3. **Shadowing**:
   ```python
   def foo():
       x = 10
       print(f'x inside foo = {x}')  # Local x
   x = 100
   foo()
   print(f'x outside foo = {x}')  # Global x
   ```

### Namespaces

- **Definition**: A namespace is a container where names (variables, functions) are mapped to objects. It allows for organized management of variable names in different scopes.
- **Global Namespace**: Contains all names defined at the top level of the script.
- **Local Namespace**: Created when a function is called and contains names defined within that function.

### Accessing Namespaces

- The Python interpreter follows a specific order to resolve names:
  1. Local namespace of the current function.
  2. Global namespace of the module.
  3. Built-in namespace.

### The `global` Keyword

- Used to declare that a variable inside a function is global and should not be treated as local. This allows you to modify the global variable inside the function.

### Built-in Functions

- Built-in functions like `print`, `int`, etc., reside in the built-in namespace. It's possible to override these names by assigning them new values, but doing so is discouraged as it can lead to errors and unexpected behavior.

### Example of Built-in Function Override

```python
print = 1  # Overrides the built-in print function
print(1)  # Raises TypeError
```

This kind of practice is strongly discouraged because it can lead to code that is difficult to debug and maintain.

### Summary

Understanding scope, local vs. global variables, and namespaces is crucial for writing effective Python code. Proper use of these concepts helps prevent errors and makes code more readable and maintainable. Always be cautious with variable names, especially when dealing with built-in functions.
