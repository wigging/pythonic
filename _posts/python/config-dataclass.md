---
title: Configuration Using a Python dataclass
date: November 21, 2024
---

A data class in Python can be used to store configuration settings for an application or service. Default configuration values are assigned to fields on the data class. However, the user can overload those values by using a class method to load the configuration settings from a file.

The configuration data class shown below defines `price` and `quantity` fields with default values. The `load_toml` class method is used to read the configuration settings from a TOML file.

```python
import tomllib
from dataclasses import dataclass


@dataclass
class Config:
    """Configuration dataclass."""

    price: float = 12.89
    quantity: int = 4

    @classmethod
    def load_toml(cls, file: str):
        """Load configuration settings from a TOML file."""

        with open(file, "rb") as f:
            conf = tomllib.load(f)

        return cls(**conf)
```

Examples of using this data class are shown next. The first example creates a config object with default values. The second example loads the configuration from a TOML file.

```python
conf = Config()

print(f"{conf.price=}")
print(f"{conf.quantity=}")

# This prints the following:
# conf.price=12.89
# conf.quantity=4

conf2 = Config.load_toml("conf.toml")

print(f"{conf2.price=}")
print(f"{conf2.quantity=}")

# This prints the following:
# conf2.price=5.99
# conf2.quantity=2
```

The contents of the TOML file used in the example is:

```toml
# Configuration settings
price = 5.99
quantity = 2
```
