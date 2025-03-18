---
title: Run Python scripts with uv
date: January 6, 2025
---

A Python script is a file intended for standalone execution. The uv tool can be used to directly run a script even if other Python packages are needed to run it. This offers a more streamlined approach for running scripts compared to manually managing a virtual environment and its dependencies.

A simple Python script that imports the NumPy package is shown below. The typical method to run this script is to create a Python virtual environment, activate the virtual environment, install the NumPy package in the environment, and finally run the script with `python hello.py`.

```python
"""Example of a simple script named ."""

import numpy as np

def main():
    print("hello there")

    a = np.array([1, 2, 3, 4, 5])
    print(f"a is {a}")

if __name__ == "__main__":
    main()
```

Alternatively, uv can be used to run the script by utilizing metadata at the top of the file as demonstrated below. The metadata defines the Python version and dependencies needed to run the script with `uv run hello.py`. The metadata can be written manually or added by uv with the `uv add --script hello.py numpy` command for this particular example. By using the inline metadata, uv will automatically install the required version of Python along with the dependencies in a virtual environment and then run the code.

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///

"""Example of a simple script."""

import numpy as np

def main():
    print("hello there")

    a = np.array([1, 2, 3, 4, 5])
    print(f"a is {a}")

if __name__ == "__main__":
    main()
```

An animated terminal session that demonstrates running the script with inline metadata is shown next. Notice how this is done with one terminal command compared to the multiple steps needed for the standard Python method discussed earlier. More information about uv is available on the Astral website at <https://astral.sh>.

<p>
<script src="https://asciinema.org/a/nefJzdwxIQldr9HmHvqiO23HH.js" id="asciicast-nefJzdwxIQldr9HmHvqiO23HH" async="true"></script>
</p>
