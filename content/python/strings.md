---
title: Strings
date: November 8, 2022
---

Some basic examples of creating strings in Python.

```python
# create a string with single quotes or double quotes
s1 = 'hello'
s2 = "hello there"

# use \ to escape a single quote or use double quotes
s3 = 'that ain\'t the one'
s4 = "that ain't the one"

# triple quotes can also be used
s5 = """another string"""
```

## String methods

Methods available for the string type are demonstrated below.

```python
# Join a list of words as a single string
>>> words = ['My', 'favorite', 'food', 'is', 'not', 'avocado']
>>> ' '.join(words)
'My favorite food is not avocado'

# Join a list of words excluding the `not` string
>>> ' '.join(filter(lambda x : x != 'not', words))
'My favorite food is avocado'
```

```python
# Split a string into a list of strings
>>> 'hello there'.split(' ')
['hello', 'there']
```

```python
# Replace the occurance of a string with another string
>>> 'hello there folks'.replace('there', 'all')
'hello all folks'
```

```python
# Remove space at beginning and end of string
>>> ' space '.strip()
'space'
```

```python
# Return a lowercase string
>>> 'Hello There'.casefold()
'hello there'
```

```python
# Check if string starts with a given prefix
>>> 'hello there'.startswith('h')
True

# Check if string ends with a given suffix
>>> 'hello there'.endswith('k')
False
```

```python
# Split lines into a list of strings
>>> """first line
    second line
    and third line""".splitlines()
['first line', 'second line', 'and third line']
```

```python
# Count the occurance of a substring
>>> 'hello there'.count('e')
3
```

```python
# Return a copy of the string where the first letter is capitalized
>>> s = 'i love apples'
>>> s.capitalize()
'I love apples'
```

```python
# Return a copy of the string where words start with an uppercase
>>> s = 'i love apples'
>>> s.title()
'I Love Apples'
```

```python
# Center a string using a fill character
>>> ' hello '.center(30, '*')
'*********** hello ************'
```

```python
# Pad a numeric string with zeros
>>> '1'.zfill(3)
'001'
```

## F-strings

```python
>>> a = 2
>>> f'you have {a} apples'
'you have 2 apples'

>>> x = 99.4
>>> f'value is {x = }'
'value is x = 99.4'
```

## Reverse a string

```python
>>> name = 'Homer'
>>> name[::-1]
'remoH'
```
