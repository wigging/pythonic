---
title: Pathlib
slug: pathlib
layout: section
date: 2020-09-12
---

The pathlib module handles file paths with support for different operating systems.

## Read text

The example below uses pathlib to read text from a file.

```python
import pathlib

text = pathlib.Path('myfile.txt').read_text()
print(text)
```

## Further reading

- Pathlib — Object-Oriented Filesystem Paths — Python 3.8.6rc1 Documentation. Accessed September 12, 2020. <https://docs.python.org/3/library/pathlib.html>
- Python 3’s Pathlib Module: Taming the File System. Real Python. Accessed September 12, 2020. <https://realpython.com/python-pathlib/>
