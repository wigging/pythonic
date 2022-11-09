---
title: Secrets
date: November 8, 2022
---

Use the `secrets` module to generate cryptographically strong random passwords containing letters, numbers, and punctuation.

```python
import string
import secrets

n = 20
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(chars) for _ in range(n))

print('password', password)
```

The code example shown above produces a 20-character password such as:

```
password ^sNw3?-!rF9U{O$J=2cW
```

or

```
password PU^1g\q6I(`lf4qz5]N[
```
