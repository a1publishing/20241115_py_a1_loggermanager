# logman

Python logging.Logger manager

## In this README :point_down:

- [Features](#features)
- [Usage](#usage)
  
  
- [FAQ](#faq)
- [Contributing](#contributing)

## Features

- get default logger
- add and store for use formatters, handlers, and loggers
- set logger level
- access logging.logger

## Usage

### Get a logger
```
>>> import logman
>>> logger_manager = logman.get_logger_manager()
>>> logger = logger_manager.get_my_logger('default_console_logger')
>>> logger.info('Created `logger_manager` and `logger`')
2024-11-15 14:50:18 INFO my_logger.py: Created `logger_manager` and `logger`
```

## FAQ

#### Is this package developed primarily for creator use?

Yes!  It's a first package published to https://pypi.org/ and as much a learning tool as anything.  That said the logger manager should be useful as a starting point for any similar project or just to avoid getting caught up in logging.Logger docs.  Use it to easily create loggers.

## Contributing

If you find a bug :bug:, have a suggestion :rocket:, etc., please let me know (<mike@a1publishing.com>)