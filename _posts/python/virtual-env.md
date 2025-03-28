---
title: Virtual Environments
date: February 16, 2024
---

The `venv` module included with Python is used to create and manage virtual environments. This page provides some useful commands for creating and working with virtual environments. A virtual environment should not be checked into source control via Git or other such systems.

Create and activate a virtual environment named "myvenv" using the commands shown below. Notice the name of the environment is "myvenv" but the name of the module is "venv".

```text
python -m venv myvenv
source myvenv/bin/activate
```

It is common to create virtual environments with the same name as the `venv` module. The commands below use "venv" and ".venv" for the environment name.

```text
python -m venv venv
source venv/bin/activate

python -m venv .venv
source .venv/bin/activate
```

Create a virtual environment with the command shown below to automatically update dependencies in the environment. This ensures that you don't have to update things like pip after you activate the environment.

```text
python -m venv --upgrade-deps venv
```

Finally, use the command shown here to deactivate the environment.

```text
deactivate
```
