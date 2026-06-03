import python017_module
import python017_module as py17
from python017_module import is_valid_password as ivp

print(python017_module.is_valid_password("safdef43"))
print(py17.is_valid_password("safdef43"))
print(ivp("safdef43"))

## oop exkurs
fahrzeug = py17.Auto("Klaus")
fahrzeug.fahre_los()
print(fahrzeug.getName())
