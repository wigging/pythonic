"""
Basic examples of creating lists.
"""

# Example 1 - create a list with square brackets
# ----------------------------------------------------------------------------

mylist = [1, 2, 3, 4, 5]

# Example 2 - unpack list values
# ----------------------------------------------------------------------------

a, b, c, = [8, 9, 10]
print('a', a)
print('b', b)
print('c', c)

first, *rest = [1, 2, 3, 4, 5, 6, 7]
print('first', first)
print('rest', rest)

first, *mid, last = [1, 2, 3, 4, 5, 6, 7]
print('first', first)
print('mid', mid)
print('last', last)

# Example 3 - enumerate a list to get index and value
# ----------------------------------------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e']

for i, x in enumerate(letters):
    print(f'index = {i} and letter = {x}')

# Example 4 - iterate over multiple lists
# ----------------------------------------------------------------------------

one = [1, 2, 3, 4, 5]
two = [2, 3, 4, 5, 6]
three = [3, 4, 5, 6, 7]

for i, j, k in zip(one, two, three):
    print('i', i, 'j', j, 'k', k)

# or use index to get each item from multiple lists
n = len(one)
for i in range(n):
    print('i', one[i], 'j', two[i], 'k', three[i])
