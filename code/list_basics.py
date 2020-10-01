"""
Basic examples of creating lists.
"""

# Create a list, indexing, slicing, and append
# ----------------------------------------------------------------------------

mylist = [1, 2, 3, 4, 5]

print('\n--- Create a list, indexing, slicing, and append ---')
print('mylist =', mylist)

# indexing returns an item in the list
print('first item =', mylist[0])
print('second item =', mylist[1])
print('last item =', mylist[-1])
print('second to last item =', mylist[-2])

# slicing returns a new list
print('slice 1: =', mylist[1:])
print('slice 1:3 =', mylist[1:3])

# append a value to end of list
mylist.append(9)
print('append 9 =', mylist)

# Combining lists
# ----------------------------------------------------------------------------

alist = [1, 2, 3]
blist = [4, 5, 6]
clist = alist + blist

print('\n--- Combining lists ---')
print('clist =', clist)

# Unpack list values
# ----------------------------------------------------------------------------

a, b, c = [8, 9, 10]

print('\n--- Unpack list values ---')
print('a =', a)
print('b =', b)
print('c =', c)

first, *rest = [1, 2, 3, 4, 5, 6, 7]
print('\n--- Unpack remaining values ---')
print('first =', first)
print('rest =', rest)

first, *mid, last = [1, 2, 3, 4, 5, 6, 7]
print('\n--- Unpack middle values ---')
print('first =', first)
print('mid =', mid)
print('last =', last)

# Enumerate a list to get index and value
# ----------------------------------------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e']

print('\n--- Enumerate a list ---')

for i, x in enumerate(letters):
    print(f'index = {i} and letter = {x}')

# Iterate over multiple lists
# ----------------------------------------------------------------------------

one = [1, 2, 3, 4, 5]
two = [2, 3, 4, 5, 6]
three = [3, 4, 5, 6, 7]

print('\n--- Iterate over several lists with zip ---')

for i, j, k in zip(one, two, three):
    print('i =', i, 'j =', j, 'k =', k)

# or use index to get each item from multiple lists
n = len(one)
print('\n--- Loop through several lists ---')

for i in range(n):
    print('i =', one[i], 'j =', two[i], 'k =', three[i])
