---
title: Delay Log File Creation
date: March 27, 2025
---

Use the delay argument for Python's log file handler to avoid creating unnecessary log files. This ensures that a log file is created only for the desired log levels.

The example below creates a logger with a file handler that only tracks critical events. However, the log file is created even if a non-critical event is logged. Consequently, an empty log file is created when messages are logged at a level that is lower than the set level.

```python
# Log file is created even for non-critical log messages

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

handler = logging.FileHandler("example.log")
logger.addHandler(handler)

logger.error("This is the error log message.")
```

Set the `delay=True` argument for the file handler to avoid creating an empty log file. This will ensure that the log file is only created when a critical-level log message occurs as shown in the example below.

```python
# Log file is only created for critical log messages

import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

handler = logging.FileHandler("example.log", delay=True)
logger.addHandler(handler)

# Create error-level log message but will not create a log file
logger.error("This is the error log message.")
print("Notice no log file has been created")
time.sleep(4)

# Create critical-level log message and will create a log file
logger.critical("This is the critical error log message.")
```

## Further Reading

See the [Basic Logging Tutorial](https://docs.python.org/3/howto/logging.html) in the Python documentation for a good overview of Python's logging features.
