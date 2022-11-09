---
title: JSON
date: November 8, 2022
---

JavaScript Object Notation (JSON) is a common data format that is supported natively in Python. The format is built on name/value pairs and ordered list values. Visit [json.org](https://www.json.org/json-en.html) to learn more about the JSON format.

## Load a JSON file

The contents of a JSON file named `books.json` are shown below:

```json
[
    {
        "title": "Alice's Adventures in Wonderland",
        "author": "Lewis Carroll",
        "year": 1865
    },
    {
        "title": "Do Androids Dream of Electric Sheep",
        "author": "Philip K. Dick",
        "year": 1968
    },
    {
        "title": "The Lorax",
        "author": "Dr. Seuss",
        "year": 1971
    }
]
```

To read this file, use the `json` module to load the contents of the file. The example below prints the title, author, and year for each book item in the JSON file.

```python
import json

with open("books.json") as json_file:
    data = json.load(json_file)

for d in data:
    print(f"{d['title']} by {d['author']} in {d['year']}")
```

This prints the following:

```
Alice's Adventures in Wonderland by Lewis Carroll in 1865
Do Androids Dream of Electric Sheep by Philip K. Dick in 1968
The Lorax by Dr. Seuss in 1971
```

## Read a JSON file containing comments

JSON does not support comments. However, commented lines in a JSON file can be ignored when reading the file line-by-line. The function shown below reads a JSON file that contains comments denoted by `//` and returns the JSON data as a dictionary. An example of using the function is also given.

```python
def read_json(jsonfile, comment='//'):
    json_str = ''

    with open(jsonfile, 'r') as json_file:
        for line in json_file:
            if comment not in line:
                json_str += line

    json_dict = json.loads(json_str)
    return json_dict
```

```python
>>> file = 'example.json'
>>> jsondict = read_json(file)
>>> jsondict[1]['first_name']
'Giavani'
```
