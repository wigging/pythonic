---
title: String
date: 2020-12-30
---

**Contents**

- [Introduction](#introduction)
- [String methods](#string-methods)

## Introduction

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
```

## F-strings

```python
>>> x = 99.4
>>> f'value is {x = }'
'value is x = 99.4'
```
