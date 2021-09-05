---
title: TOML
date: 2021-09-05
---

With the `toml` package, the contents of a TOML file can be loaded into a Python dictionary. Below is an example of reading a TOML file named `configure.toml` into a `config` dictionary.

```toml
# This is a comment in a TOML file named configure.toml

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
ports = [8000, 8001, 8002]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]

[servers.alpha]
ip = "10.0.0.1"     # This is an inline comment
role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"
```

```python
import toml

# Load the TOML file into a dictionary

with open('configure.toml', 'r') as f:
    config = toml.load(f)

# Print out values from the TOML dictionary

print('title is:\t\t', config['title'])
print('ports are:\t\t', config['database']['ports'])
print('servers alpha role is:\t', config['servers']['alpha']['role'])
```

The above Python code prints the following:

```
title is:               TOML Example
ports are:              [8000, 8001, 8002]
servers alpha role is:  frontend
```
