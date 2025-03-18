---
title: Pre-allocate a Python list
date: November 8, 2022
---

If the size of a list is known, then pre-allocating the list can provide performance improvements; especially for a large list. The example below measures the performance of appending items to an empty list. Pre-allocating a list of known size and assigning items to it gives better performance than appending to the list. The list comprehension approach (see Example 3) gives the best elapsed time.

- Example 1 = 11.6552 ms
- Example 2 = 8.9583 ms
- Example 3 = 4.5061 ms

```python
import time

# Size of the list
n = 100_000

# Example 1. Create an empty list and append items to it.
# ----------------------------------------------------------------------------

tic = time.perf_counter_ns()

list_one = []

for i in range(n):
    list_one.append(i)

toc = time.perf_counter_ns()
print(f'Ex 1 elapsed time {(toc - tic) / 1_000_000:.4f} ms')
print(f'list_one = {list_one[:3]}...{list_one[-3:]}\n')

# Example 2. Pre-allocate list of None items then assign items at each index.
# ----------------------------------------------------------------------------

tic = time.perf_counter_ns()

list_two = [None] * n

for i in range(n):
    list_two[i] = i

toc = time.perf_counter_ns()
print(f'Ex 2 elapsed time {(toc - tic) / 1_000_000:.4f} ms')
print(f'list_two = {list_two[:3]}...{list_two[-3:]}\n')

# Example 3. Pre-allocate list and assign items using list comprehension.
# ----------------------------------------------------------------------------

tic = time.perf_counter_ns()

list_three = [i for i in range(n)]

toc = time.perf_counter_ns()
print(f'Ex 3 elapsed time {(toc - tic) / 1_000_000:.4f} ms')
print(f'list_three = {list_three[:3]}...{list_three[-3:]}')
```
