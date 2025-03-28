---
title: Sublime Text for Python Projects
date: November 25, 2023
---

Projects in [Sublime Text](https://www.sublimetext.com) are made up of two files: the `.sublime-project` file, which contains the project configuration, and the `.sublime-workspace` file, which contains user specific data such as the open files and the modifications to each file.

Below is a project file (`myproj.sublime-project`) that sets the max line length for the flake8 linter to 110. This is done by defining the flake8 settings for the LSP-pylsp package. Notice the folders path is defined as the current directory because the file resides in the top-level of the Python project.

```text
my-project/
├── README.md
├── example.py
└── myproj.sublime-project
```

```json
// myproj.sublime-project

{
    "folders":
    [
        {
            "path": "."
        }
    ],
    "settings": {
        "LSP": {
            "LSP-pylsp": {
                "settings": {
                    "pylsp.plugins.flake8.maxLineLength": 110
                }
            }
        }
    }
}
```

Below is a Sublime Text project file that uses [ruff](https://github.com/astral-sh/ruff) for Python linting and sets its max line length to 110. This is done by defining the settings for the LSP-pylsp package.

```json
{
    "folders":
    [
        {
            "path": "."
        }
    ],
    "settings": {
        "LSP": {
            "LSP-pylsp": {
                "settings": {
                    "pylsp.configurationSources": ["ruff"],
                    "pylsp.plugins.pycodestyle.enabled": false,
                    "pylsp.plugins.flake8.enabled": false,
                    "pylsp.plugins.pyflakes.enabled": false,
                    "pylsp.plugins.mccabe.enabled": false,
                    "pylsp.plugins.pyls_isort.enabled": false,
                    "pylsp.plugins.ruff.enabled": true,
                    "pylsp.plugins.ruff.lineLength": 110
                }
            }
        }
    }
}
```
