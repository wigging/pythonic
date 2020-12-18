"""
Use pathlib to read text from a file.
"""

import pathlib

text = pathlib.Path('myfile.txt').read_text()

print(text)
