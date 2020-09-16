"""
Several ways to reverse a list.
"""

# Example 1
# ----------------------------------------------------------------------------

# Reverse a list in-place. Fast and does not take up extra memory. Modifies
# original list.

list_one = [1, 2, 3, 4, 5]
list_one.reverse()

print('list_one\n', list_one)

# Example 2
# ----------------------------------------------------------------------------

# Slicing creates a reversed copy of the list. Takes up memory but doesn't
# modify the original list.

list_two = [6, 7, 8, 9, 10]
list_three = list_two[::-1]

print('list_three\n', list_three)

# Example 3
# ----------------------------------------------------------------------------

# Returns an iterator that returns elements in reverse order. Does not modify
# original list. Needs to be converted into a list object again.

list_four = [11, 12, 13, 14, 15]
list_five = list(reversed(list_four))

print('list_five\n', list_five)
