---
title: Package name
date: June 11, 2023
---

The distribution name of a Python package can be different than the import name. Below is an example of a repository named `sklearn-model` which contains the `skmodel` package.

```text
sklearn-model/
├── README.md
├── examples/
│   └── example.py
├── pyproject.toml
└── src/
    └── skmodel/
        ├── __init__.py
        └── adder.py
```

The contents of the `pyproject.toml` are shown below. Notice the distribution name is defined as `sklearn-model` which is the name displayed on PyPI and is the name shown by the `pip list` command. However, the package is imported by the user with `import skmodel` because it lives in the `src/skmodel` directory.

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "sklearn-model"
version = "0.1"
```
