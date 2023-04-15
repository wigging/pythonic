"""
Given the string 'Mary had a little Mommy lamb', count the number of times a
letter appears in the string.
"""

from collections import Counter

orig_phrase = 'Mary had a little Mommy lamb'

# Example 1
# Remove all white space then count letters.
# ----------------------------------------------------------------------------

print('Example 1 -', orig_phrase)

phrase = orig_phrase.replace(' ', '')

for p in phrase:
    print(p, phrase.count(p))

# Example 2
# Remove all white space, use Counter, then count letters
# ----------------------------------------------------------------------------

print('Example 2 -', orig_phrase)

phrase = orig_phrase.replace(' ', '')
counter = Counter(phrase)

for c in counter:
    print(c, counter[c])

# Example 3
# Remove all white space with walrus operator then count letters.
# ----------------------------------------------------------------------------

print('Example 3 -', orig_phrase)

for p in (phrase := orig_phrase.replace(' ', '')):
    print(p, phrase.count(p))

# Example 4
# Remove all white space then use list comprehension to count letters.
# ----------------------------------------------------------------------------

print('Example 4 -', orig_phrase)

phrase = orig_phrase.replace(' ', '')
[print(p, phrase.count(p)) for p in phrase]

# Example 5
# Remove all white space, use lower case, then count letters.
# ----------------------------------------------------------------------------

print('Example 5 -', orig_phrase)

phrase = orig_phrase.replace(' ', '').lower()

for p in phrase:
    print(p, phrase.count(p))

# Example 6
# Remove all white space, use lower case, use Counter, sort counter, then
# count the letters in order.
# ----------------------------------------------------------------------------

print('Example 6 -', orig_phrase)

phrase = orig_phrase.replace(' ', '').lower()
counter = Counter(phrase)

for c in sorted(counter):
    print(c, counter[c])
