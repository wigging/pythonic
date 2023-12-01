---
title: Version number
date: November 30, 2023
---

Use the [importlib.metadata](https://docs.python.org/3/library/importlib.metadata.html) library in Python to get the version number of a package. The example below gets the version of the ipython package that has been installed in the environment.

```python
>>> from importlib.metadata import version
>>> version('ipython')
'8.15.0'
```

In a package, instead of defining `__version__` somewhere in the package, the version number can just be defined in the `pyproject.toml` file as shown below. Then `importlib.metadata` can be used to get the version number of that package. This approach has been adopted by [Flask](https://github.com/pallets/flask/pull/5242/files).

```toml
[project]
name = "MyPackage"
version = "3.1"
```
