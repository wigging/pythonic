"""
Unpack contents of a tuple.
"""

# Example 1
# ----------------------------------------------------------------------------

x = 'one', 'two', 'three'
a, b, c = x

print('a =', a)
print('b =', b)
print('c =', c)

# Example 2
# ----------------------------------------------------------------------------

y = 4, 5, 6, 7, 8, 9
s, *t, u = y

print('s =', s)
print('t =', t)
print('u =', u)
