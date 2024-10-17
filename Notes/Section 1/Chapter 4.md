# Strings in Python

## Quotes: Single, Double, and Triple

A string in Python can be enclosed in single (`'`), double (`"`), or triple quotes (`'''` or `"""`). Triple quotes are typically used for multi-line strings.

Example:

```python
x = '''first line
second line
third line'''
print(x)
```

Output:

```python
first line
second line
third line
```

## Length of Strings

Use the `len()` function to determine the length of a string.

Example:

```python
x = 'good'
print(len(x))  # Output: 4
```

## Operations on Strings

1. **Concatenation:** Using the `+` operator.

   ```python
   string1 = 'first'
   string2 = ','
   string3 = 'second'
   result = string1 + string2 + string3
   print(result)  # Output: first,second
   ```

2. **Replication:** Using the `*` operator to repeat a string.

   ```python
   s = 'good'
   print(s * 5)  # Output: goodgoodgoodgoodgood
   ```

3. **Comparison:** Using `==`, `>`, `<` operators for lexicographic comparisons.

   ```python
   print('good' > 'bad')  # Output: True
   ```

## Escape Characters

The backslash (`\`) is used to introduce special characters.

- `\n` for newline
- `\t` for tab
- `\'` for escaping single quotes

Example:

```python
print('This is the first line.\nThis is the second line.')
```

Output:

```python
This is the first line.
This is the second line.
```

## Substrings

The `in` keyword checks if a string is a substring of another.

Example:

```python
a = 'good'
b = 'very good'
print(a in b)  # Output: True
```

## Indexing and Slicing

Strings support both positive and negative indexing. The first character has index `0`, and the last has index `-1`.

Example:

```python
word = 'world'
print(word[0])   # Output: w
print(word[-1])  # Output: d
```

**Slicing:** To extract a portion of a string.

```python
email = 'CS_10_014@iitm.ac.in'
roll = email[6:9]  # Output: 014
```

## Immutability of Strings

Strings are immutable in Python, meaning their contents cannot be changed once created.

Example:

```python
word = 'hello'
word[0] = 'H'  # This will raise an error
```

## String Methods

- `capitalize()`: Capitalizes the first letter.
- `isalpha()`: Checks if all characters are alphabetic.

Example:

```python
sentence = 'hello world'
print(sentence.capitalize())  # Output: Hello world

name = 'John'
print(name.isalpha())  # Output: True
```
