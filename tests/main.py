from register_value import register_value as rv
from fun import get_lr

rv.register('lr', 0.01)
print(f'lr: {get_lr()}')
