"""
Example of fizz buzz.
"""

for i in range(1, 35):
    if i % 15 == 0:
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
