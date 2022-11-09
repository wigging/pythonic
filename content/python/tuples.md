---
title: Tuples
date: November 8, 2022
---

A tuple is a number of items separated by commas.

```python
# create a tuple with or without parentheses
t1 = 1.34, 'hello', 'there'
t2 = (1.34, 'hello', 'there')
```

Tuples can be unpacked to assign items to variables.

```python
# Example 1 - unpack each item to a variable
# ----------------------------------------------------------------------------

x = 'one', 'two', 'three'
a, b, c = x

print('a =', a)
print('b =', b)
print('c =', c)

# Example 2 - unpack first, middle, and last items
# ----------------------------------------------------------------------------

y = 4, 5, 6, 7, 8, 9
s, *t, u = y

print('s =', s)
print('t =', t)
print('u =', u)
```

## Further reading

- Data Structures — Python 3.8.6rc1 Documentation. Accessed September 17, 2020. <https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences>
