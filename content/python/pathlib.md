+++
title = "Pathlib"
date = 2022-11-08
+++

The `pathlib` module handles file paths with support for different operating systems.

## Read text

The example below uses pathlib to read text from a file.

```python
>>> import pathlib
>>> pathlib.Path('myfile.txt').read_text()
'text contained in the file'
```

## File name

Get the file name from a given path.

```python
>>> import pathlib
>>> file = '/Users/gavinw/Desktop/screenshot.png'
>>> pathlib.Path(file).name
'screenshot.png'
```
