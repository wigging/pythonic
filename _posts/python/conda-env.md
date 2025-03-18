---
title: Conda environments
date: June 15, 2023
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

If you want to run a single command using a conda environment (but don't want to activate the environment first), you can use `conda run` as shown below:

```bash
# Run a command in an environment without activating the environment first
$ conda run -n myenv python --version
```
