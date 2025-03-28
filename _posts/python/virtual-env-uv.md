---
title: Virtual Environments with uv
date: January 5, 2025
---

The uv tool is a great option for installing Python and creating virtual environments. It will automatically install Python if it is not available on your system.

The typical Python installation and virtual environment workflow consists of the steps shown below. There are different ways to install Python depending on the operating system and additional steps must be taken if multiple versions of Python are needed.

1. Install a Python version
2. Create and activate a virtual environment
3. Install dependencies with pip
4. Run your Python code

With uv, the process is similar as before (see steps below). However, installing Python is simplified with uv because it will automatically install the latest version if it does not exist on the system. Uv can also manage different Python versions without additional tools.

1. Install uv
2. Create and activate a virtual environment
3. Install dependencies with pip
4. Run your Python code

Below is a terminal session where uv creates a virtual environment for running a Python script. The `--seed` option ensures that pip is available in the environment. Use the `--python` option to specify a particular Python version to use for the virtual environment. More information about uv is available on the Astral website at <https://astral.sh>.

<p>
<script src="https://asciinema.org/a/5uZe2fUWRh8QSQVJ5yesDeEgb.js" id="asciicast-5uZe2fUWRh8QSQVJ5yesDeEgb" async="true"></script>
</p>
