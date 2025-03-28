---
title: Python Projects with uv
date: January 7, 2025
---

Managing a virtual environment and its dependencies can be a hassle for Python projects. Choosing between the different techniques to install Python and different package managers can be a daunting task. Luckily, uv makes this process much easier.

The uv tool manages the Python installation, dependencies, and virtual environment for a project. To create a Python project, use `uv init myproject` to initialize the project in the `myproject` directory. This will create several files as shown in the tree diagram below.

```text
myproject/
├── .git/
├── .gitignore
├── .python-version
├── README.md
├── hello.py
└── pyproject.toml
```

To add dependencies like ruff and NumPy to the project, run the `uv add ruff numpy` command. This will create a virtual environment, add packages to the environment and the `pyproject.toml` file, and create a `uv.lock` file in the project directory (see below). Use the `uv run hello.py` command to run the `hello.py` script using the project's virtual environment.

```toml
[project]
name = "myproject"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "numpy>=2.2.1",
    "ruff>=0.8.6",
]
```

```text
myproject/
├── .git/
├── .gitignore
├── .python-version
├── .venv/          <-- virtual environment for dependencies
├── README.md
├── hello.py
├── pyproject.toml
└── uv.lock         <-- lock file for reproducible installs
```

An example of this workflow is demonstrated in the terminal session shown below. Notice that uv will also initialize the project as a git repository. More information about uv is available on the Astral website at <https://astral.sh>.

<p>
<script src="https://asciinema.org/a/xoT3NKFJfcxp1eN4ovG60iqda.js" id="asciicast-xoT3NKFJfcxp1eN4ovG60iqda" async="true"></script>
</p>
