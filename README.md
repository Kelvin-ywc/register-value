# RegisterValue
A lightweight Python library that uses the Singleton pattern to create a RegisterValue class for storing specific values, such as configuration parameters or other values used in multiple places. The value can be accessed by importing the package, eliminating the need to repeatedly pass parameters, thus reducing code complexity.

## Installation
```angular2html
pip install register-value
```

## Qiuck Start
```python
# register value
from register_value import register_value as rv
rv.register('key', 'value')
```

```python
# access value
from register_value import register_value as rv
value = rv.get('key')
```

## Application
Considering that we have two files, main.py and fun.py.
### main.py
```python
from register_value import register_value as rv
from fun import get_lr

rv.register('lr', 0.01)
print(f'lr: {get_lr()}')

```
### fun.py
```python
from register_value import register_value as rv

def get_lr():
    return rv.get('lr')
```
As we can see, in the fun.py, we get parameter lr through the register_value package, instead of passing it as a parameter. This will simplify the code specially in the huge project.