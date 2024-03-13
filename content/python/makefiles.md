---
title: Makefiles
date: March 12, 2024
---

Makefiles are typically used for C and C++ projects to build source code but they can be useful for Python projects too. A Makefile is just a text file used by the GNU Make tool to run commands. For a Python project, these commands can run unit tests, format your code, or publish a package to PyPI.

A rule in a Makefile is structured as shown below. A *target* is the name of a file or the name of an action to carry out. A *dependency* or *prerequisite* is a file that is used as input to create the target (this is optional). The *command* or *recipe* is an action that Make carries out. Note that commands are indented with a tab (not spaces).

```text
target: dependencies ...
    commands
    ...
```

The content of a simple Makefile that can be used for a Python project is shown below. Use the `make` command in the terminal to execute a target in the file. For example, run `make check` to perform the linter and formatter checks with the ruff tool, run `make test` to use pytest, run `make clean` to remove the cache directories.

```makefile
check:
    ruff check .
    ruff format --check .

clean:
    rm -rf .ruff_cache
    rm -rf .pytest_cache
    rm -rf __pycache__

test:
    pytest --verbose --cache-clear
```

## Example

A Makefile example for Python is available in the `pythonic/python-projects/makefile-project` directory on [GitHub](https://github.com/wigging/pythonic). The file structure for the example is shown here along with the contents of the Makefile. Settings for the ruff linter are in the `pyproject.toml`.

```text
makefile-project/
├── Makefile
├── main.py
├── pyproject.toml
└── test_adder.py
```

```makefile
# Contents of the Makefile

help:
    @printf "\nCommands:\n"
    @printf "\033[32mcheck\033[0m   ruff linter and formatter checks\n"
    @printf "\033[32mclean\033[0m   delete cache directories\n"
    @printf "\033[32mtest\033[0m    run unit tests with pytest\n"

check:
    ruff check .
    ruff format --check .

clean:
    rm -rf .ruff_cache
    rm -rf .pytest_cache
    rm -rf __pycache__

test:
    pytest --verbose --cache-clear
```

Running `make check` in the `makefile-project` directory should output the linter warnings shown below. Running `make test` should display a failed pytest and running `make clean` will remove the cache directories created by ruff and pytest.

```text
$ make check

ruff check .
main.py:1:1: D100 Missing docstring in public module
main.py:1:17: F401 [*] `numpy` imported but unused
main.py:11:5: D400 First line should end with a period
main.py:11:5: D401 First line of docstring should be in imperative mood: "here"
test_adder.py:1:1: D100 Missing docstring in public module
test_adder.py:3:5: D103 Missing docstring in public function
Found 6 errors.
[*] 1 fixable with the `--fix` option (1 hidden fix can be enabled with the `--unsafe-fixes` option).
make: *** [check] Error 1
```

Run `make` or `make help` to print the help information to the screen (shown below). When `make` is run without specifying a target, it executes the first target in the Makefile; which is the `help` target in this example.

```text
Commands:
check   ruff linter and formatter checks
clean   delete cache directories
test    run unit tests with pytest
```
