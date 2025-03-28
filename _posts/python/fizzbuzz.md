---
title: Fizz Buzz in Python
date: May 14, 2020
---

This is the classic fizz buzz example where a number divisible by 3 is replaced with Fizz, a number divisible by 5 is replaced with Buzz, and a number divisible by both 3 and 5 (divisible by 15) is replaced with Fizz Buzz.

```python
for i in range(1, 35):
    if i % 15 == 0:
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
```

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz Buzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
Fizz Buzz
31
32
Fizz
34
```
