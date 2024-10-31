### Function Calling

1. **Basic Function Calls**:

   - The example demonstrates how functions can call each other. When `first()` is executed, it calls `second()`, which in turn calls `third()`.
   - The output order is `third`, `second`, `first`, illustrating the call stack: the last function called completes first, and control returns to the previous function.

2. **Traffic-Signal Method**:

   - Functions can be in three states: ongoing, suspended, or completed.
     - **Ongoing**: When control is inside the function and executing code.
     - **Completed**: When all lines have been executed, and control has exited the function.
     - **Suspended**: When a function calls another function and awaits its completion.

3. **Stack Representation**:
   - The stack visualizes the state of function calls at different times, showing how control flows between functions as they complete.

### Recursion

1. **Recursive Functions**:

   - A function that calls itself, such as the factorial function `fact()`.
   - It includes a **base case** to terminate recursion; without it, recursion can lead to infinite calls.

2. **Example of Factorial Calculation**:

   - The function halts execution temporarily to execute `fact(n - 1)` until reaching `fact(0)`, which returns `1`, allowing the stack to unwind.

3. **Fibonacci Series**:

   - Demonstrates another recursive function, `fibo()`, to compute Fibonacci numbers.
   - The naive recursive implementation can lead to excessive computation and inefficiency due to repeated calculations of the same values (e.g., `fibo(2)` is calculated multiple times).

4. **Performance Measurement**:

   - The time taken for a function to run can be measured using the `time` library.
   - The naive recursive solution for Fibonacci is inefficient, especially for large inputs.

5. **Iterative Solution**:
   - An iterative approach to the Fibonacci series avoids the inefficiency of recursion by maintaining state with variables.

### Counting Function Calls

- A global variable can be used to count how many times a function has been called, demonstrated with the factorial example.

### Infinite Recursion and Errors

1. **Pathological Recursion**:
   - A function without a base case can lead to a `RecursionError` due to exceeding the maximum recursion depth (typically 1000 in Python).
   - Checking the recursion limit can be done using `sys.getrecursionlimit()`.

### Summary

- This content serves as an introduction to understanding function calls and recursion in Python. It explains key concepts such as the call stack, function states, recursive versus iterative approaches, performance issues, and potential pitfalls like infinite recursion.
