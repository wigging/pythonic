---
title: Conda environments
date: November 5, 2022
---

Similar to Python's `venv` module, Conda can also create virtual environments but these environments support languages other than Python.

```bash
# Create a Python environment named `myenv`, can also use `-n` for `--name`
$ conda create --name myenv python

# Activate the `myenv` environment
$ conda activate myenv

# Command prompt for the activated environment
(myenv) $

# Deactivate the current environment
(myenv) $ conda deactivate

# Remove an environment named `myenv`, can also use `-n` for `--name`
$ conda env remove --name myenv

# Create an environment using a config file
$ conda env create --file environment.yml
```
