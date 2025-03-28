---
title: Count Letters with Python
date: April 15, 2023
---

Given the string `Mary had a little Mommy lamb`, count the number of times a letter appears in the string. See the examples below for different approaches.

## Basic example

This example uses a for-loop to print and count each letter in the string. All white space is removed from the string.

```python
orig_phrase = 'Mary had a little Mommy lamb'

phrase = orig_phrase.replace(' ', '')

for p in phrase:
    print(p, phrase.count(p))
```

The output from this example is shown below. Every letter in the string is printed along with the number of times the letter appears in the string. Notice the count for each letter is case-sensitive.

```
M 2
a 4
r 1
y 2
h 1
a 4
d 1
a 4
l 3
i 1
t 2
t 2
l 3
e 1
M 2
o 1
m 3
m 3
y 2
l 3
a 4
m 3
b 1
```

## Counter example

This example is similar to the previous example except a `Counter` object is used to count the letters in the string.

```python
from collections import Counter

orig_phrase = 'Mary had a little Mommy lamb'

phrase = orig_phrase.replace(' ', '')
counter = Counter(phrase)

for c in counter:
    print(c, counter[c])
```

Output from this example is shown below. The upper and lower case letters are printed once along with the number of times that letter appears in the string. Notice the count for each letter is case-sensitive.

```
M 2
a 4
r 1
y 2
h 1
d 1
l 3
i 1
t 2
e 1
o 1
m 3
b 1
```

## Walrus example

The walrus operator is used in this example to assign the string to a variable. All white space is removed from the string.

```python
orig_phrase = 'Mary had a little Mommy lamb'

for p in (phrase := orig_phrase.replace(' ', '')):
    print(p, phrase.count(p))
```

The output from this example is shown below. Every letter in the string is printed along with the number of times the letter appears in the string. Just like the previous examples, the count for each letter is case-sensitive.

```
M 2
a 4
r 1
y 2
h 1
a 4
d 1
a 4
l 3
i 1
t 2
t 2
l 3
e 1
M 2
o 1
m 3
m 3
y 2
l 3
a 4
m 3
b 1
```

## List comprehension example

A list comprehension is used in this example to print and count the letters in a string. All white space is removed from the string.

```python
orig_phrase = 'Mary had a little Mommy lamb'

phrase = orig_phrase.replace(' ', '')
[print(p, phrase.count(p)) for p in phrase]
```

The output is shown below. Every letter in the string is printed along with the number of times the letter appears in the string. The count for each letter is case-sensitive.

```
M 2
a 4
r 1
y 2
h 1
a 4
d 1
a 4
l 3
i 1
t 2
t 2
l 3
e 1
M 2
o 1
m 3
m 3
y 2
l 3
a 4
m 3
b 1
```

## Lowercase example

In this example, all the letters are made lowercase and white space is removed from the string.

```python
orig_phrase = 'Mary had a little Mommy lamb'

phrase = orig_phrase.replace(' ', '').lower()

for p in phrase:
    print(p, phrase.count(p))
```

The output is shown below. Every letter in the string is printed along with the number of times the letter appears in the string. Notice the count is not case-sensitive because the string is lowercase.

```
m 5
a 4
r 1
y 2
h 1
a 4
d 1
a 4
l 3
i 1
t 2
t 2
l 3
e 1
m 5
o 1
m 5
m 5
y 2
l 3
a 4
m 5
b 1
```

## Lowercase counter example

All the letters in this example are lowercase and white space is removed from the string. A `Counter` object is used to count the letters in the string and the results are sorted alphabetically.

```python
from collections import Counter

orig_phrase = 'Mary had a little Mommy lamb'

phrase = orig_phrase.replace(' ', '').lower()
counter = Counter(phrase)

for c in sorted(counter):
    print(c, counter[c])
```

Output from this example is shown below. Each letter is printed once along with the number of times that letter appears in the string. The count is not case-sensitive because the string is lowercase.

```
a 4
b 1
d 1
e 1
h 1
i 1
l 3
m 5
o 1
r 1
t 2
y 2
```
