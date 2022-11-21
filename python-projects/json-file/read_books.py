"""
Load the contents of the `books.json` file and print the book title, author,
and year.
"""

import json

with open("books.json") as json_file:
    data = json.load(json_file)

for d in data:
    print(f"{d['title']} by {d['author']} in {d['year']}")
