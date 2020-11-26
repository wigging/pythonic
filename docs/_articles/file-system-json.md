---
title: JSON with comments
date: 2020-10-04
---

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
