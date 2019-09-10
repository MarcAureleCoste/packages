# Simple Packages
Project to explain packages.

When installed this package give you three commands:
 - now      : Return the current datetime
 - hour+1   : Return the current datetime plus 1 hour
 - hour-1   : Return the current datetime minus 1 hour

You can also import and use the function `str_to_datetime`

```python
from simple_package import str_to_datetime

str_to_datetime('2019-01-01')
```

This function take a string and return the datetime object representation.

## Build

```sh
python setup.py build
```

## Install (build not required)

```sh
pip install .
```

## Install for development (build not required)

```sh
pip install -e .
```