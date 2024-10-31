# Math And Programming

Before closing this chapter, let us spend some time at the intersection of mathematics and programming.

## Limits

Consider the following number:

It is known that \( \sqrt{2} - 1 \). From this, it follows that \( \sqrt{2} - 1 < 1 \). Now, consider the following sequence:

As \( n \) becomes very large, the values in this sequence will become smaller and smaller. This is because if you keep multiplying a fraction by itself, it becomes smaller and smaller. In mathematical terms, the limit of this sequence as \( n \) tends to infinity is zero. Let us verify this programmatically:

```python
import math
n = int(input())                # sequence length
CONST = math.pow(2, 0.5) - 1    # basic term in the sequence
a_n = 1                         # zeroth term
for i in range(n):
    a_n = a_n * CONST           # computing the nth term
print(a_n)
```

Try this out for a few values of \( n \). For \( n = 50 \), the value is approximately \( 1.4210854715202342 \times 10^{-14} \), which is so small that for all practical purposes, it is as good as zero.

## Recurrence Relation

Now, here is another fact. For every number \( n \), there are unique integers \( x_n \) and \( y_n \) such that:

\[
x*n = 2y*{n-1} - x*{n-1} \quad \text{and} \quad y_n = x*{n-1} - y\_{n-1}
\]

For \( n = 1 \), this is obvious: \( x_1 = -1 \) and \( y_1 = 1 \). What about higher values of \( n \)? We can prove this using mathematical induction. The following is a sketch of the inductive proof. If \( n \geq 1 \), then:

The equations given above define what is called a recurrence relation: each new term in the sequence is a function of the preceding terms. In this sequence, we have \( x_n \) and \( y_n \) defined as above. For \( n \), the pair of equations forms the recurrence relation:

```python
n = int(input())    # sequence length
x_n, y_n = -1, 1    # x_1 and y_1
for i in range(n - 1):
    x_n, y_n = 2 * y_n - x_n, x_n - y_n
```

## Rational Approximation

This provides a way to approximate \( \sqrt{2} \) using rational numbers:

As \( n \) becomes large, this approximation will become increasingly accurate. For example, here is an approximation after 100 iterations. It is accurate up to several decimal places!

Is any of this useful? I don't know. But honestly, who cares? We don't do things because they are useful. We do them because they are interesting. And all interesting things will find their use at some point in the future.
