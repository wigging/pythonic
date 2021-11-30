---
title: Strings
date: 2021-11-29
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
>>> s = 'i love apples'

# return a copy of the string where the first letter is capitalized
>>> s.capitalize()
'I love apples'

# return a copy of the string where words start with an uppercase
>>> s.title()
'I Love Apples'

# center a string using a fill character
>>> ' hello '.center(30, '*')
'*********** hello ************'

# pad a numeric string with zeros
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

## Join strings

```python
>>> words = ['My', 'favorite', 'food', 'is', 'not', 'avocado']
>>> ' '.join(words)
'My favorite food is not avocado'

>>> ' '.join(filter(lambda x : x != 'not', words))
'My favorite food is avocado'
```

