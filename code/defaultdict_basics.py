"""
Examples of using defaultdict which supplies missing values.
"""

from collections import defaultdict

# using defaultdict will return a default value for the missing key
dd = defaultdict(int)
print('defaultdic', dd['item'])

# using a regular dictionary will return a key error
d = {}
print('dict', d['item'])
